%global tar_name py3exiv2

Name:           python3-exiv2
Version:        0.7.2
Release:        3%{?dist}
License:        GPLv2+ and GPLv3+
Summary:        Python3 bindings for the exiv2 library
Url:            https://launchpad.net/py3exiv2

Source:         https://files.pythonhosted.org/packages/source/p/py3exiv2/%{tar_name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  boost-python3-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(exiv2)
BuildRequires:  python3-rpm-macros
BuildRequires:  python3-devel

%description
python3-exiv2 is a Python 3 binding to exiv2, the C++ library for manipulation
of EXIF, IPTC and XMP image metadata. It is a python 3 module that allows your
scripts to read and write metadata (EXIF, IPTC, XMP, thumbnails) embedded in
image files (JPEG, TIFF, ...).

It is designed as a high-level interface to the functionalities offered by
libexiv2. Using python’s built-in data types and standard modules, it provides
easy manipulation of image metadata.

%prep
%autosetup -n %{tar_name}-%{version} -p1

%build
# Workaround as there is no -lboost_python3
sed -i 's|boost_python3|boost_python%{python3_version_nodots}|' setup.py
%py3_build

%install
%py3_install

%files
%doc README
%{python3_sitearch}/*

%changelog
* Sat May 30 2020 Jonathan Wakely <jwakely@redhat.com> - 0.7.2-3
- Rebuilt for Boost 1.73

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.7.2-2
- Rebuilt for Python 3.9

* Mon Apr 27 2020 Andreas Schneider <asn@redhat.com> - 0.7.2-1
- Update to version 0.7.2

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.1-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.1-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 05 2019 Andreas Schneider <asn@redhat.com> - 0.7.1-1
- Update to version 0.7.1

* Tue Apr 09 2019 Andreas Schneider <asn@redhat.com> - 0.6.1-1
- Update to version 0.6.1
  * Add the streaming of the preview data

* Thu Jan 31 2019 Andreas Schneider <asn@redhat.com> - 0.5.0-1
- Update to version 0.5.0
  * Several bugfixes for exiv2-0.27

* Wed Jan 30 2019 Rex Dieter <rdieter@fedoraproject.org> - 0.3.0-5
- rebuild (exiv2)

* Wed Jan 30 2019 Jonathan Wakely <jwakely@redhat.com> - 0.3.0-4
- Rebuilt for Boost 1.69

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Miro Hrončok <mhroncok@redhat.com> - 0.3.0-2
- Rebuilt for Python 3.7

* Thu Jun 28 2018 Andreas Schneider <asn@redhat.com> - 0.3.0-1
- Update to version 0.3.0

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.2.1-4
- Rebuilt for Python 3.7

* Tue May 08 2018 Andreas Schneider <asn@redhat.com> - 0.2.1-3
- Added missing dist tag to Release

* Mon May 07 2018 Andreas Schneider <asn@redhat.com> - 0.2.1-2
- Fixed license
- Removed build requires for gcc-c++

* Sun May 06 2018 Andreas Schneider <asn@redhat.com> - 0.2.1-1
- Initial package
