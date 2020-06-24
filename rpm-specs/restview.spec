%global pypi_name restview

Name:           %{pypi_name}
Version:        2.9.2
Release:        2%{?dist}
Summary:        ReStructuredText viewer

License:        GPLv3+
URL:            https://mg.pov.lt/restview/
Source0:        %{pypi_source}
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3-docutils
BuildRequires:  python3-mock
BuildRequires:  python3-pygments
BuildRequires:  python3-readme-renderer
BuildRequires:  python3-setuptools

Requires:       python3-%{pypi_name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description
A viewer for ReStructuredText documents that renders them on the fly. Pass
the name of a ReStructuredText document to restview, and it will launch a
web server on localhost:random-port and open a web browser. Every time you
reload the page, restview will reload the document from disk and render it.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
A library for ReStructuredText documents that renders them.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files
%{_bindir}/%{pypi_name}

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py*.egg-info/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.9.2-2
- Rebuilt for Python 3.9

* Mon Mar 02 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.9.2-1
- Initial package for Fedora
