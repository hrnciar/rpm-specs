# Upstream does not release tarballs.  Instead the code is copied directly
# into the polymake distribution.  Therefore, we check out the code from git.
%global commit  031cc3a0a7c125060951d9e8b0ca67a5091cc5ac
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global gitdate 20190509

%global srcname JuPyMake

Name:           python-jupymake
Version:        0.9
Release:        9.%{gitdate}.%{shortcommit}%{?dist}
Summary:        Python wrapper for the polymake shell

License:        GPLv2+
URL:            https://github.com/sebasguts/JuPyMake
Source0:        %{url}/archive/%{commit}/%{srcname}-%{shortcommit}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  libnormaliz-devel
BuildRequires:  python3-devel
BuildRequires:  polymake

%global _description %{expand:
This package provides a basic interface to call polymake from python.
It is meant to be used in the Jupyter interface for polymake.}

%description %_description

%package     -n python3-jupymake
Summary:        Python wrapper for the polymake shell
Requires:       polymake%{?_isa}

# This can be removed when Fedora 31 reaches EOL
Obsoletes:      python3-%{srcname} < 0.9
Provides:       pytnon3-%{srcname} = %{version}-%{release}

%description -n python3-jupymake %_description

%prep
%autosetup -n %{srcname}-%{commit}

%build
%py3_build

%install
%py3_install

%files       -n python3-jupymake
%doc README README.md example.py
%license COPYING GPLv2 LICENSE
%{python3_sitearch}/%{srcname}*

%changelog
* Wed Sep 30 2020 Jerry James <loganjerry@gmail.com> - 0.9-9.20190509.031cc3a
- Rebuild for normaliz 3.8.9

* Mon Sep 28 2020 Jerry James <loganjerry@gmail.com> - 0.9-8.20190509.031cc3a
- Rebuild for polymake 4.2

* Mon Aug 31 2020 Jerry James <loganjerry@gmail.com> - 0.9-7.20190509.031cc3a
- Rebuild for normaliz 3.8.8

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-6.20190509.031cc3a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Jerry James <loganjerry@gmail.com> - 0.9-5.20190509.031cc3a
- Rebuild for polymake 4.1

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.9-4.20190509.031cc3a
- Rebuilt for Python 3.9

* Wed Mar  4 2020 Jerry James <loganjerry@gmail.com> - 0.9-3.20190509.031cc3a
- Rebuild for polymake 4.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-2.20190509.031cc3a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 25 2019 Jerry James <loganjerry@gmail.com> - 0.9-1.20190509.031cc3a
- Initial RPM
