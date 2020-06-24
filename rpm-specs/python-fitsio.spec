%global srcname fitsio
%global sum A full featured python library to read from and write to FITS files


Name:           python-%{srcname}
Version:        1.0.3
Release:        6%{?dist}
Summary:        %{sum}

License:        GPLv2+
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://files.pythonhosted.org/packages/source/f/%{srcname}/%{srcname}-%{version}.tar.gz

# Patch to force usage of Fedora cfitsio instead of bundled copy
Patch0:         %{name}-use-system-cfitsio.patch

# General
BuildRequires:  cfitsio-devel
BuildRequires:  gcc
# Python 3
BuildRequires:  python3-devel
BuildRequires:  python3-numpy


%description
%{sum}.

%package -n python3-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python3-%{srcname}}
Requires:       python3-numpy

%description -n python3-%{srcname}
%{sum}.


%prep
%setup -q -n %{srcname}-%{version}
%patch0 -p1

%build
sed -i "s,@INCLUDEDIR@,%{_includedir}/cfitsio,g" setup.py
sed -i "s,@LIBDIR@,%{_libdir},g" setup.py
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%license LICENSE.txt
%doc README.md
%{python3_sitearch}/*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.3-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.3-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.3-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 02 2019 Christian Dersch <lupinix@fedoraproject.org> - 1.0.3-1
- new version

* Sun Apr 28 2019 Christian Dersch <lupinix@mailbox.org> - 1.0.1-1
- new version

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 02 2018 Christian Dersch <lupinix@fedoraproject.org> - 0.9.11-9
- drop python2 subpackage (#1627411)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.9.11-7
- Rebuilt for Python 3.7

* Sat May 26 2018 Christian Dersch <lupinix@mailbox.org> - 0.9.11-6
- rebuilt for cfitsio 3.450

* Fri Feb 23 2018 Christian Dersch <lupinix@mailbox.org> - 0.9.11-5
- rebuilt for cfitsio 3.420 (so version bump)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Apr 06 2017 Christian Dersch <lupinix@mailbox.org> - 0.9.11-1
- new version

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.9.10-2
- Rebuild for Python 3.6

* Sat Oct 01 2016 Christian Dersch <lupinix@mailbox.org> - 0.9.10-1
- Initial package


