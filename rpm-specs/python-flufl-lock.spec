%global srcname flufl.lock
%global pkgname flufl-lock
%global summary NFS-safe file locking with timeouts for POSIX systems
%global _description \
The flufl.lock library provides an NFS-safe file-based locking algorithm \
influenced by the GNU/Linux "open(2)" man page, under the description of \
the "O_EXCL" option.


Name:           python-%{pkgname}
Version:        3.2
Release:        10%{?dist}
Summary:        %{summary}

License:        ASL 2.0
URL:            https://gitlab.com/warsaw/flufl.lock
Source0:        https://files.pythonhosted.org/packages/source/f/%{srcname}/%{srcname}-%{version}.tar.gz
Source1:        https://gitlab.com/warsaw/flufl.lock/raw/master/LICENSE
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
cp -p %{SOURCE1} .


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
rm -rf %{buildroot}%{_prefix}/lib/python*/site-packages/flufl/lock/{*.rst,docs,conf.py}


%check
%{__python3} setup.py test
%if 0%{?with_python3_other}
%{__python3_other} setup.py test
%endif


%files -n python%{python3_pkgversion}-%{pkgname}
%license LICENSE
%doc README.rst flufl/lock/NEWS.rst flufl/lock/docs/using.rst
%{python3_sitelib}/flufl/
%{python3_sitelib}/%{srcname}-%{version}*-py%{python3_version}.egg-info/
%{python3_sitelib}/%{srcname}-%{version}*-py%{python3_version}-nspkg.pth

%if 0%{?with_python3_other}
%files -n python%{python3_other_pkgversion}-%{pkgname}
%license LICENSE
%doc README.rst flufl/lock/NEWS.rst flufl/lock/docs/using.rst
%{python3_other_sitelib}/flufl/
%{python3_other_sitelib}/%{srcname}-%{version}*-py%{python3_other_version}.egg-info/
%{python3_other_sitelib}/%{srcname}-%{version}*-py%{python3_other_version}-nspkg.pth
%endif


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.2-9
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.2-7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.2-6
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.2-2
- Rebuilt for Python 3.7

* Thu Feb 15 2018 Aurelien Bompard <abompard@fedoraproject.org> - 3.2-1
- Version 3.2

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Aurelien Bompard <abompard@fedoraproject.org> - 2.4.1-5
- Fix BuildRequires name

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.4.1-2
- Rebuild for Python 3.6

* Wed Sep 14 2016 Aurelien Bompard <abompard@fedoraproject.org> - 2.4.1-1
- Initial package.
