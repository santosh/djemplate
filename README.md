# personalweb

personalweb serves as persoanl website boilerplate, made in Django. This includes a homepage, a blog, a projects section and a contact section. If it seems good for your use, go grab it. 

## Getting Started

Make a virtual environment if you haven't already so that you're not messing up your system level packages. Install packages with `pip install -r requirements.txt`.

    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt

Then you run as with any other Django application.

    python manage.py runserver

If you are interested in deploying to cloud, see Deployment section in GitHub wiki.

## Development

Necessary dependencies.

 * `Django`
 * `Pillow` - For handling images in blog post (ORM)
 * `pymongo` - other can be used too, unless you know how to deal with it

Development dependencies.

 * `pylint` - spot the error until it's too late
 * `autopep8` - so that you don't have to remember every moves

Found a bug? Have an idea? Create an [issue](https://github.com/santosh/personalweb/issues). Seel also [CONTRUBUTING](./.github/CONTRIBUTING.md).

## License

This project is licensed under BSD-3. See [LICENSE](./LICENSE) for full license.