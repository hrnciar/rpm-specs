%global pypi_name zuul-client

Name:       python-%{pypi_name}
Version:    0.0.2
Release:    1%{?dist}
Summary:    The zuulclient Python module
License:    ASL 2.0
URL:        https://zuul-ci.org

Source0:    %pypi_source

Source1:    fake-zuul-client

BuildArch:  noarch

%description
The zuulclient Python module is a client library for
Zuul Gating System's REST API. It includes zuul-client,
a CLI utility to interact with Zuul instances.

%package -n python3-%{pypi_name}
Summary: %summary
BuildRequires:  python3dist(testtools)
BuildRequires:  python3dist(stestr)
BuildRequires: python3-devel
BuildRequires: python3dist(requests)
# Doc requirements
BuildRequires:  python3dist(zuul-sphinx)
BuildRequires:  python3dist(sphinx-autodoc-typehints)
BuildRequires:  python3dist(sphinxcontrib-blockdiag)
BuildRequires:  python3dist(sphinxcontrib-programoutput)
BuildRequires:  python3dist(reno)

%py_provides python3-%{pypi_name}

%prep
%autosetup -n %{pypi_name}-%{version}

%description -n python3-%{pypi_name}
The zuulclient Python module is a client library for
Zuul Gating System's REST API. It includes zuul-client,
a CLI utility to interact with Zuul instances.

%package doc
Summary: zuul-client documentation

%description doc
Documentation for the zuulclient library and the zuul-client CLI.

%build
%py3_build

cp %{SOURCE1} build/zuul-client
chmod +x build/zuul-client
# Generate documentation (without release note because source doesn't have git log)
sed -e 's/^ *releasenotes$//' -i doc/source/index.rst
rm doc/source/releasenotes.rst
# Build HTML doc
PYTHONPATH=../../build/lib PATH=$PATH:$(pwd)/build PBR_VERSION=%{version} SPHINX_DEBUG=1 sphinx-build-3 \
    -b html doc/source build/html
# Remove empty stub files
find build -type f -name "*.pyi" -size 0 -delete
# rm doc build leftovers
rm -Rf build/html/.buildinfo build/html/.doctrees
# Fix file-not-utf8
iconv -f iso8859-1 -t utf-8 build/html/objects.inv > build/html/objects.inv.conv && \
    mv -f build/html/objects.inv.conv build/html/objects.inv
# Fix wrong-file-end-of-line-encoding
sed -i 's/\r$//' LICENSE
sed -i 's/\r$//' build/html/objects.inv

%install
%py3_install

%check
PYTHON=%{__python3} stestr run

%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{_bindir}/*
%{python3_sitelib}/zuulclient
%{python3_sitelib}/zuul_client*.egg-info

%files doc
%license LICENSE
%doc build/html

%changelog
* Thu Oct  1 2020 Matthieu Huin <mhuin@redhat.com> - 0.0.2-1
- Initial packaging
