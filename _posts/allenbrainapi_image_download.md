---
layout: post
title: "AllenBrainAPI_image_download"
tags:
    - python
    - notebook
---
# Introduction

My goal is to make a python library for programmatically accessing features of
the Allen Brain Institute API ([website](http://help.brain-
map.org//display/api/Downloading+an+Image)).

I will follow a RESTful style if possible. See [this
website](http://rest.elkstein.org/2008/02/what-is-rest.html) for more details on
REST.




# Implementing AtlasImage Download Service

[URL](http://help.brain-map.org//display/api/Downloading+an+Image)

From the website:
The AtlasImage download service serves whole and partial two-dimensional images
with annotations presented on the Allen Brain Atlas Web site.

Our prototype call is of the form

http://api.brain-map.org/api/v2/atlas_image_download/[AtlasImage.id]?downsample=
[#]&quality=[#]&annotation=[true|false]&atlas=[#]

Calling the API via the above URL returns a jpeg image.

We have the following parameters:


<h3><a name="DownloadinganImage-Parameters"></a>Parameters</h3>

<div class='table-wrap'>
<table class='confluenceTable'><tbody>
<tr>
<td class='confluenceTd'> filename </td>
<td class='confluenceTd'> Integer </td>
<td class='confluenceTd'> AtlasImage.id identifying the image to download. </td>
</tr>
<tr>
<td class='confluenceTd'> annotation </td>
<td class='confluenceTd'> Boolean (optional) </td>
<td class='confluenceTd'> Set the value to true to retrieve the specified
AtlasImage with annotations. </td>
</tr>
<tr>
<td class='confluenceTd'> atlas </td>
<td class='confluenceTd'> Integer (optional) </td>
<td class='confluenceTd'> Specify the desired Atlas.ID for the annotations. The
P56 Adult Mouse Brain Atlas and Developing Mouse Brain Atlas share a common
AtlasDataSet, so the Atlas.ID should be specified.&nbsp; </td>
</tr>
<tr>
<td class='confluenceTd'> downsample </td>
<td class='confluenceTd'> Integer (optional) </td>
<td class='confluenceTd'> The number of times to downsample the original image.
For example, 'downsample=1' halves the number of pixels of the original image
both horizontally and vertically. Specifying 'downsample=2' quarters the height
and width values. </td>
</tr>
<tr>
<td class='confluenceTd'> quality </td>
<td class='confluenceTd'> Integer (optional) </td>
<td class='confluenceTd'> The jpeg quality of the returned image. This must be
an integer from 0, for the lowest quality, up to as high as 100. If it is not
specified, it defaults to the highest quality. </td>
</tr>
<tr>
<td class='confluenceTd'> left </td>
<td class='confluenceTd'> Integer (optional) </td>
<td class='confluenceTd'> Index of the leftmost column of the region of
interest, specified in full-resolution (largest tier) pixel coordinates.
SectionImage.x is the default value. </td>
</tr>
<tr>
<td class='confluenceTd'> top </td>
<td class='confluenceTd'> Integer (optional) </td>
<td class='confluenceTd'> Index of the topmost row of the region of interest,
specified in full-resolution (largest tier) pixel coordinates. SectionImage.y is
the default value. </td>
</tr>
<tr>
<td class='confluenceTd'> width </td>
<td class='confluenceTd'> Integer (optional) </td>
<td class='confluenceTd'> Number of columns in the output image, specified in
tier-resolution (desired tier) pixel coordinates. SectionImage.width is the
default value. It is automatically adjusted when downsampled. </td>
</tr>
<tr>
<td class='confluenceTd'> height </td>
<td class='confluenceTd'> Integer (optional) </td>
<td class='confluenceTd'> Number of rows in the output image, specified in tier-
resolution (desired tier) pixel coordinates. SectionImage.height is the default
value. It is automatically adjusted when downsampled. </td>
</tr>
</tbody></table>
</div>


#Make a Request
To make a call to the Allen API I'll use the python library 'Requests'
(http://docs.python-requests.org/en/latest/index.html).

Note: for the first part of these notes where I'm going through the various ways
to use the requests library, I'll be pretty much copy and pasting parts from the
[Requests quickstart page](http://docs.python-
requests.org/en/latest/user/quickstart/).

I'll start by trying to download the downsampled AtlasImage 100883869 with
annotations which has the url

http://api.brain-
map.org/api/v2/atlas_image_download/100883869?downsample=4&annotation=true


Let's first import requests.

**In []:**

{% highlight python %}

{% endhighlight %}

Let's try and get the completed image download URL.

**In []:**

{% highlight python %}

{% endhighlight %}

Now we have a Response object called r.


**In []:**

{% highlight python %}

{% endhighlight %}

#Passing Parameters In URLs
We want a way to choose our id, so we use % to substitute elements of our dict
into the string:

**In []:**

{% highlight python %}

{% endhighlight %}

    http://api.brain-map.org/api/v2/atlas_image_download/100883869?downsample=4&annotation=true


Requests also gives us a way to do this by specifying what to put after the ? in
the URL.

**In []:**

{% highlight python %}

{% endhighlight %}

**In []:**

{% highlight python %}

{% endhighlight %}

**In []:**

{% highlight python %}

{% endhighlight %}

    http://api.brain-map.org/cgi-bin/imageservice?mime=1&path=/external/0350/prod34/0205081399/0205081399_devmouse_rendered.aff&left=3008&top=30592&width=969&height=489&downsample=4


which gives us a correct URL to download the image from the Allen API.

Let's try to put this together and clean it up:

**In []:**

{% highlight python %}

{% endhighlight %}

    http://api.brain-map.org/cgi-bin/imageservice?mime=1&path=/external/0350/prod34/0205081399/0205081399_devmouse_rendered.aff&left=3008&top=30592&width=969&height=489&downsample=4


TODO: The above code is a little better but what I would really like to do is
create an object 'AtlasImage' and give it the attributes of id, downsample,
annotation, and anything else. Probably the way to this is by constructing a
new-style class (see [this site](https://stackoverflow.com/questions/61517
/python-dictionary-from-an-objects-fields) also [this](http://goodcode.io/blog
/python-dict-object/))


#Response Content

We can read the content of the server's response.


**In []:**

{% highlight python %}

{% endhighlight %}

If we want to be able to be able to work with the jpg instead of just
downloading it, we will need to decode it. If we look at the raw contents of r
we get a lot of junk for the `_contents` section (because of the jpeg gzip
encoding) and then some useful stuff at the bottom (scroll all the way down).

**In []:**

{% highlight python %}

{% endhighlight %}

Requests automatically decodes the gzip transfer-encoding so we don't need to
worry about that. In order to get the image then we will use PIL, numpy, and
matplotlib's pyplot.

**In []:**

{% highlight python %}

{% endhighlight %}

Success!

#Response Status Codes

We can check the response status code:

**In []:**

{% highlight python %}

{% endhighlight %}

Requests also comes with a built-in status code lookup object for easy
reference:


**In []:**

{% highlight python %}

{% endhighlight %}

If we made a bad request (a 4XX client error or 5XX server error response), we
can raise it with **Response.raise_for_status():**

**In []:**

{% highlight python %}

{% endhighlight %}

**In []:**

{% highlight python %}

{% endhighlight %}

**In []:**

{% highlight python %}

{% endhighlight %}

    ---------------------------------------------------------------------------
    HTTPError                                 Traceback (most recent call last)

    <ipython-input-16-cdf6910f7d4c> in <module>()
    ----> 1 bad_r.raise_for_status()
    

    /usr/local/lib/python2.7/dist-packages/requests/models.pyc in raise_for_status(self)
        793 
        794         if http_error_msg:
    --> 795             raise HTTPError(http_error_msg, response=self)
        796 
        797     def close(self):


    HTTPError: 404 Client Error: Not Found

But, since our status_code for r was 200, when we call raise_for_status() we
get:

**In []:**

{% highlight python %}

{% endhighlight %}

As expected we get no output.

#Response Headers

We can view the server’s response headers using a Python dictionary:

**In []:**

{% highlight python %}

{% endhighlight %}

The dictionary is special, though: it’s made just for HTTP headers. According to
RFC 7230, HTTP Header names are case-insensitive.

So, we can access the headers using any capitalization we want:

**In []:**

{% highlight python %}

{% endhighlight %}

**In []:**

{% highlight python %}

{% endhighlight %}

#Errors and Exceptions

In the event of a network problem (e.g. DNS failure, refused connection, etc),
Requests will raise a ConnectionError exception.

In the rare event of an invalid HTTP response, Requests will raise an
**HTTPError** exception.

If a request times out, a **Timeout** exception is raised.

If a request exceeds the configured number of maximum redirections, a
**TooManyRedirects** exception is raised.

All exceptions that Requests explicitly raises inherit from
**requests.exceptions.RequestException**.
