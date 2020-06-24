# Not building on EPEL 6 due to incompatibility with Werkzeug < 0.9:
# https://github.com/Runscope/httpbin/issue/317

# Not building on EPEL 7 as brotli is not built for it

%global modname httpbin

%global desc Testing an HTTP Library can become difficult sometimes. RequestBin is \
fantastic for testing POST requests, but doesn't let you control the response. \
This exists to cover all kinds of HTTP scenarios. Additional endpoints are \
being considered. All endpoint responses are JSON-encoded.

# Disable Python 2 builds for Fedora > 29, EPEL > 7
%if 0%{?fedora} > 29 || 0%{?rhel} > 7
%bcond_with         python2
%global obsolete2   1
%else
%bcond_without      python2
%global obsolete2   0
%endif

# Requirements for tests (BuildRequires) and run (Requires)
# EPEL builds do not provide python2-*
# blinker is required by raven[flask], but python-raven package does
# not depend on it, so we require it here
%global t_requires python2-brotli python2-flask python2-markupsafe python2-decorator python2-itsdangerous python2-blinker python2-raven python2-six python2-werkzeug
%global t3_requires python3-blinker python3-brotli python3-flask python3-markupsafe python3-decorator python3-itsdangerous python3-raven python3-six python3-werkzeug

Name:           python-%{modname}
Version:        0.7.0
Release:        11%{?dist}
Summary:        HTTP Request & Response Service, written in Python + Flask

License:        MIT
URL:            https://github.com/Runscope/httpbin
Source0:        %{url}/archive/v%{version}/%{modname}-%{version}.tar.gz
# Use the Google 'brotli' module, not 'brotlipy'
# When I asked why this uses brotlipy, upstream (Cory Benfield) said:
# "The upstream Brotli module is a hand-coded C extension to Python.
# This has a number of downsides, but the major one is that it ruins
# performance on PyPy. As an avid user of PyPy, I want something I can
# deploy there. Hence: brotlipy, which uses CFFI."
# For me that's not enough of a reason to bother packaging it.
Patch1:         0001-Use-Google-s-brotli-module-not-the-brotlipy-one.patch

# Drop content length == 0 asserts, to support werkzeug>=0.15.1
# From https://github.com/postmanlabs/httpbin/pull/555
Patch2:         0002-Drop-content-length-0-asserts.patch
BuildArch:      noarch


%description
%{desc}

%if 0%{?with_python2}
%package -n python2-%{modname}
Summary:        %{summary}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  %{t_requires}
Requires:       %{t_requires}
%{?python_provide:%python_provide python2-%{modname}}

%description -n python2-%{modname}
%{desc}

This package provides the Python 2 implementation.
%endif # with python2

%package -n python3-%{modname}
Summary:        %{summary}
BuildRequires:  python3-setuptools
BuildRequires:  python3-devel
BuildRequires:  %{t3_requires}
Requires:       %{t3_requires}
%{?python_provide:%python_provide python3-%{modname}}
%if 0%{?obsolete2}
Obsoletes:      python2-%{modname} < %{version}-%{release}
%endif # obsolete2

%description -n python3-%{modname}
%{desc}

This package provides the Python 3 implementation.

#################################################################################
%prep
%autosetup -n %{modname}-%{version} -p1
# no need for this to be executable
chmod ugo-x httpbin/templates/forms-post.html

%build
%if 0%{?with_python2}
%py2_build
%endif # with python2
%py3_build

%install
%if 0%{?with_python2}
%py2_install
%endif # with python2
%py3_install

#################################################################################
%check
%if 0%{?with_python2}
%{__python2} test_httpbin.py
%endif # with python2
%{__python3} test_httpbin.py

#################################################################################
%if 0%{?with_python2}
%files -n python2-%{modname}
%{python2_sitelib}/%{modname}*
%license LICENSE
%doc README.md AUTHORS
%endif # with python2

%files -n python3-%{modname}
%{python3_sitelib}/%{modname}*
%license LICENSE
%doc README.md AUTHORS

#################################################################################
%changelog
* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 0.7.0-11
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.0-9
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Sat Aug 17 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.0-8
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 23 2018 Adam Williamson <awilliam@redhat.com> - 0.7.0-5
- Disable Python 2 build on F30+, EL8+
- Drop all the EPEL compat stuff for now as we can't build for EPEL

* Sun Nov 18 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.7.0-4
- Drop explicit locale setting
  See https://fedoraproject.org/wiki/Changes/Remove_glibc-langpacks-all_from_buildroot

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Miro Hrončok <mhroncok@redhat.com> - 0.7.0-2
- Rebuilt for Python 3.7

* Thu May 10 2018 Adam Williamson <awilliam@redhat.com> - 0.7.0-1
- Update to 0.7.0, drop merged patch, update requirements

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 16 2017 Adam Williamson <awilliam@redhat.com> - 0.6.2-3
- Use and require Google's 'brotli', not brotlipy's 'brotli' (wat)
- Require python(3)-blinker, as raven[flask] requires it

* Thu Nov 16 2017 Adam Williamson <awilliam@redhat.com> - 0.6.2-2
- Drop flask-limiter requirement (which broke the whole thing...)

* Fri Oct 20 2017 Adam Williamson <awilliam@redhat.com> - 0.6.2-1
- Update to 0.6.2

* Wed Aug 30 2017 Adam Williamson <awilliam@redhat.com> - 0.6.1-1
- Update to 0.6.1
- Remove EL 6 compatibility bits (probably won't ever build on EL 6)
- Remove apparently useless upstream requirement for flask-common

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 31 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.5.0-6
- Cleanups in spec
- Remove useless (and broken) requires on python3-pkgversion-macros

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 10 2017 Adam Williamson <awilliam@redhat.com> - 0.5.0-4
- Conditionalize argparse dependency as it disappeared from Rawhide

* Wed Dec 21 2016 Adam Williamson <awilliam@redhat.com> - 0.5.0-3
- properly own all directories
- fix the mode of a template (doesn't need to be executable)

* Wed Dec 21 2016 Adam Williamson <awilliam@redhat.com> - 0.5.0-2
- add missing runtime deps to python3 package
- add comment explaining use of LANG

* Wed Dec 21 2016 Adam Williamson <awilliam@redhat.com> - 0.5.0-1
- initial package
