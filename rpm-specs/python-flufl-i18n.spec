%global srcname flufl.i18n
%global pkgname flufl-i18n
%global summary A high level API for Python internationalization
%global _description \
The ``flufl.i18n`` library provides a convenient API for managing translation \
contexts in Python applications. It provides facilities not only for          \
single-context applications like command line scripts, but also more          \
sophisticated management of multiple-context applications such as Internet    \
servers.

Name:           python-%{pkgname}
Version:        2.0.2
Release:        3%{?dist}
Summary:        %{summary}

License:        ASL 2.0
URL:            https://gitlab.com/warsaw/flufl.i18n
Source0:        https://files.pythonhosted.org/packages/source/f/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python-srpm-macros
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-atpublic
%if 0%{?with_python3_other}
BuildRequires:  python%{python3_other_pkgversion}-devel
BuildRequires:  python%{python3_other_pkgversion}-setuptools
BuildRequires:  python%{python3_other_pkgversion}-atpublic
%endif

%description %{_description}


%package -n python%{python3_pkgversion}-%{pkgname}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pkgname}}
Requires:       python%{python3_pkgversion}-setuptools
Requires:       python%{python3_pkgversion}-atpublic

%description -n python%{python3_pkgversion}-%{pkgname} %{_description}


%if 0%{?with_python3_other}
%package -n python%{python3_other_pkgversion}-%{pkgname}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_other_pkgversion}-%{pkgname}}
Requires:       python%{python3_other_pkgversion}-setuptools
Requires:       python%{python3_other_pkgversion}-atpublic

%description -n python%{python3_other_pkgversion}-%{pkgname} %{_description}
%endif


%prep
%autosetup -n %{srcname}-%{version}


%build
%py3_build
%if 0%{?with_python3_other}
%py3_other_build
%endif


%install
%py3_install
%if 0%{?with_python3_other}
%py3_other_install
%endif

# This will go in %%doc
rm -rf %{buildroot}%{_prefix}/lib/python*/site-packages/flufl/i18n/{*.rst,docs,conf.py}


%check
%{__python3} setup.py test
%if 0%{?with_python3_other}
%{__python3_other} setup.py test
%endif


%files -n python%{python3_pkgversion}-%{pkgname}
%license LICENSE
%doc flufl/i18n/*.rst flufl/i18n/docs/*.rst
%{python3_sitelib}/flufl/
%{python3_sitelib}/%{srcname}-%{version}*-py%{python3_version}.egg-info/
%{python3_sitelib}/%{srcname}-%{version}*-py%{python3_version}-nspkg.pth

%if 0%{?with_python3_other}
%files -n python%{python3_other_pkgversion}-%{pkgname}
%license LICENSE
%doc flufl/i18n/*.rst flufl/i18n/docs/*.rst
%{python3_other_sitelib}/flufl/
%{python3_other_sitelib}/%{srcname}-%{version}*-py%{python3_other_version}.egg-info/
%{python3_other_sitelib}/%{srcname}-%{version}*-py%{python3_other_version}-nspkg.pth
%endif


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0.2-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 30 2019 Aurelien Bompard <abompard@fedoraproject.org> - 2.0.2-1
- Version 2.0.2

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.1-6
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.0.1-2
- Rebuilt for Python 3.7

* Wed Feb 14 2018 Aurelien Bompard <abompard@fedoraproject.org> - 2.0.1-1
- Version 2.0.1

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Aurelien Bompard <abompard@fedoraproject.org> - 1.1.3-5
- Fix BuildRequires name

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.1.3-2
- Rebuild for Python 3.6

* Wed Sep 14 2016 Aurelien Bompard <abompard@fedoraproject.org> - 1.1.3-1
- Initial package.
