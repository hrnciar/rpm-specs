%global pkgname aiosmtpd
%global summary Asyncio-based SMTP server
%global _description \
This is a server for SMTP and related protocols, similar in utility \
to the standard library’s smtpd.py module, but rewritten to be based \
on asyncio for Python 3.
%global srcname %{pkgname}
%global with_docs 0


Name:           python-%{pkgname}
Version:        1.2.1
Release:        7%{?dist}
Summary:        %{summary}

License:        ASL 2.0
URL:            https://github.com/aio-libs/aiosmtpd
Source0:        https://github.com/aio-libs/aiosmtpd/archive/%{version}.tar.gz
BuildArch:      noarch
# Fix expired testing SSL certs
Patch0:         f414dcdc0312c4cf3f3d39deb3ea7d15e89a5334.patch
# Fix tests on Python 3.8
# https://github.com/aio-libs/aiosmtpd/pull/169
Patch1:         4a80b454a164278a4751c761b64305a325abc5f0.patch


BuildRequires:  python-srpm-macros
BuildRequires:  python%{python3_pkgversion}-devel >= 3.4
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-atpublic
BuildRequires:  python%{python3_pkgversion}-nose2
BuildRequires:  python%{python3_pkgversion}-flufl-testing
%if 0%{?with_docs}
BuildRequires:  python%{python3_pkgversion}-sphinx
%endif
%if 0%{?with_python3_other}
BuildRequires:  python%{python3_other_pkgversion}-devel >= 3.4
BuildRequires:  python%{python3_other_pkgversion}-setuptools
BuildRequires:  python%{python3_other_pkgversion}-atpublic
BuildRequires:  python%{python3_other_pkgversion}-nose2
BuildRequires:  python%{python3_other_pkgversion}-flufl-testing
%endif

%description %{_description}


%package -n python%{python3_pkgversion}-%{pkgname}
Summary:        %{summary}
Requires:       python%{python3_pkgversion}-atpublic
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pkgname}}

%description -n python%{python3_pkgversion}-%{pkgname} %{_description}


%if 0%{?with_python3_other}
%package -n python%{python3_other_pkgversion}-%{pkgname}
Summary:        %{summary}
Requires:       python%{python3_other_pkgversion}-atpublic
%{?python_provide:%python_provide python%{python3_other_pkgversion}-%{pkgname}}

%description -n python%{python3_other_pkgversion}-%{pkgname} %{_description}
%endif


%prep
%autosetup -p1 -n %{srcname}-%{version}


%build
%py3_build
%if 0%{?with_python3_other}
%py3_other_build
%endif
%if 0%{?with_docs}
%{__python3} setup.py build_sphinx
%endif


%install
%py3_install
# Cleanups
rm -rf %{buildroot}%{python3_sitelib}/examples
rm -f  %{buildroot}%{python3_sitelib}/aiosmtpd/docs/.gitignore

%if 0%{?with_python3_other}
%py3_other_install
# Avoid name clash
mv %{buildroot}%{_bindir}/aiosmtpd \
   %{buildroot}%{_bindir}/aiosmtpd-%{python3_other_version}
# Cleanups
rm -rf %{buildroot}%{python3_other_sitelib}/examples
rm -f  %{buildroot}%{python3_other_sitelib}/aiosmtpd/docs/.gitignore
%endif


%check
%{__python3} -m nose2 -v
%if 0%{?with_python3_other}
%{__python3_other} -m nose2 -v
%endif


%files -n python%{python3_pkgversion}-%{pkgname}
%doc README.rst examples
%if 0%{?with_docs}
%doc build/sphinx/html
%endif
%{_bindir}/aiosmtpd
%{python3_sitelib}/*

%if 0%{?with_python3_other}
%files -n python%{python3_other_pkgversion}-%{pkgname}
%doc README.rst examples build/sphinx/html
%{_bindir}/aiosmtpd-%{python3_other_version}
%{python3_other_sitelib}/*
%endif


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.2.1-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 30 2019 Aurelien Bompard <abompard@fedoraproject.org> - 1.2.1-2
- Fix build

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.1-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 20 2018 Aurelien Bompard <abompard@fedoraproject.org> - 1.2.1-1
- Update to 1.2.1.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0-5
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jun 03 2017 Aurelien Bompard <abompard@fedoraproject.org> - 1.0-0.1.a5
- Update to 1.0 final.

* Mon Apr 10 2017 Aurelien Bompard <abompard@fedoraproject.org> - 1.0-0.1.a5
- Update to 1.0a5.

* Wed Dec 14 2016 Aurelien Bompard <abompard@fedoraproject.org> - 1.0-0.1.a4
- Initial package.
