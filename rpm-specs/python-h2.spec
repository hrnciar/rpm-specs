# Created by pyp2rpm-3.3.2
%global pypi_name h2

%global common_description %{expand:
HTTP/2 Protocol Stack This repository contains a pure-Python
implementation of a HTTP/2 protocol stack. It's written from the ground up to
be embeddable in whatever program you choose to use, ensuring that you can
speak HTTP/2 regardless of your programming paradigm.}

%bcond_without docs

Name:           python-%{pypi_name}
Version:        3.2.0
Release:        3%{?dist}
Summary:        HTTP/2 State-Machine based protocol implementation

License:        MIT
URL:            http://hyper.rtfd.org
Source0:        %pypi_source
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  (python3dist(hpack) >= 2.3 with python3dist(hpack) < 4)
BuildRequires:  (python3dist(hyperframe) >= 5.2 with python3dist(hyperframe) < 6)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(hypothesis)

%if %{with docs}
# Unbundle
BuildRequires:  js-jquery
BuildRequires:  js-underscore
%endif

%{?python_enable_dependency_generator}

%description
%{common_description}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%{common_description}

%if %{with docs}
%package doc
Summary:        Documentation for %{name}

Requires: js-jquery
Requires: js-underscore

%description doc
%{common_description}

This is the documentation package for h2.
%endif

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%if %{with docs}
# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

# Unbundle JS
rm -f html/_static/underscore.js
ln -s /usr/share/javascript/underscore/underscore-min.js html/_static/underscore.js
rm -f html/_static/underscore-1.3.1.js
ln -s /usr/share/javascript/underscore/underscore.js html/_static/underscore-1.3.1.js
rm -f html/_static/jquery.js
ln -s /usr/share/javascript/jquery/3.2.1/jquery.min.js html/_static/jquery.js
rm -f html/_static/jquery-3.2.1.js
ln -s /usr/share/javascript/jquery/3.2.1/jquery.js html/_static/jquery-3.2.1.js
%endif

%install
%py3_install

%check
%{__python3} -m pytest

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py*.egg-info

%if %{with docs}
%files doc
%doc html
%license LICENSE
%endif


%changelog
* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 3.2.0-3
- Rebuilt for Python 3.9

* Mon Feb 17 03:14:38 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 3.2.0-1
- Update to 3.2.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Sep 18 2019 Robert-André Mauchin <zebob.m@gmail.com> - 3.1.1-1
- Release 3.1.1 (#1742451)

* Mon Sep 09 2019 Miro Hrončok <mhroncok@redhat.com> - 3.1.0-6
- Subpackage python2-h2 has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Aug 17 2019 Miro Hrončok <mhroncok@redhat.com> - 3.1.0-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.1.0-3
- Rebuilt to update automatic Python dependencies

* Fri Mar 08 2019 Jeroen van Meeuwen <vanmeeuwen+fedora@kolabsys.com> - 3.1.0-2
- Add bcond_without docs

* Thu Mar 07 2019 Robert-André Mauchin <zebob.m@gmail.com> - 3.1.0-1
- Release 3.1.0
- Run tests

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.0.1-2
- Rebuilt for Python 3.7

* Mon May 14 2018 Robert-André Mauchin <zebob.m@gmail.com> - 3.0.1-1
- Initial package.
