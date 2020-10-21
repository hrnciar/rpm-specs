%global py2_incdir %(python2 -c 'import distutils.sysconfig; print(distutils.sysconfig.get_python_inc())')
%global py2_libbuilddir %(python2 -c 'import sys; import sysconfig; print("lib.{p}-{v[0]}.{v[1]}".format(p=sysconfig.get_platform(), v=sys.version_info))')

%global srcname pillow

Name:           python2-%{srcname}
Version:        6.2.2
Release:        3%{?dist}
Summary:        Python image processing library

# License: see http://www.pythonware.com/products/pil/license.htm
License:        MIT
URL:            http://python-pillow.github.io/
Source0:        https://github.com/python-pillow/Pillow/archive/%{version}/Pillow-%{version}.tar.gz

BuildRequires:  freetype-devel
BuildRequires:  gcc
BuildRequires:  ghostscript
BuildRequires:  lcms2-devel
BuildRequires:  libimagequant-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libraqm-devel
BuildRequires:  libtiff-devel
BuildRequires:  libwebp-devel
BuildRequires:  openjpeg2-devel
BuildRequires:  tk-devel
BuildRequires:  zlib-devel

BuildRequires:  python2-devel
BuildRequires:  python2-numpy
BuildRequires:  python2-olefile
BuildRequires:  python2-setuptools

# For EpsImagePlugin.py
Requires:       ghostscript

Provides:       python2-imaging = %{version}-%{release}
# For MicImagePlugin.py, FpxImagePlugin.py
Requires:       python2-olefile

%global __provides_exclude_from ^%{python2_sitearch}/PIL/.*\\.so$

%description
Python image processing library, fork of the Python Imaging Library (PIL)

This library provides extensive file format support, an efficient
internal representation, and powerful image processing capabilities.

This is a minimal compatibility package for https://pagure.io/fesco/issue/2266


%prep
%autosetup -p1 -n Pillow-%{version}


%build
# Build Python 2 modules
%py2_build


%install
# Install Python 2 modules
install -d %{buildroot}/%{py2_incdir}/Imaging
install -m 644 src/libImaging/*.h %{buildroot}/%{py2_incdir}/Imaging
%py2_install

# Drop files which used to be in subpackages which are not provided anymore
rm -rf %{buildroot}%{python2_sitearch}/PIL/_imagingtk*
rm -rf %{buildroot}%{python2_sitearch}/PIL/ImageTk*
rm -rf %{buildroot}%{python2_sitearch}/PIL/SpiderImagePlugin*
rm -rf %{buildroot}%{python2_sitearch}/PIL/ImageQt*

# Drop devel-files
rm -rf %{buildroot}%{py2_incdir}/Imaging/


%check
# Check Python 2 modules
ln -s $PWD/Images $PWD/build/%py2_libbuilddir/Images
cp -R $PWD/Tests $PWD/build/%py2_libbuilddir/Tests
cp -R $PWD/selftest.py $PWD/build/%py2_libbuilddir/selftest.py
pushd build/%py2_libbuilddir
PYTHONPATH=$PWD %{__python2} selftest.py
popd


%files -n python2-%{srcname}
%doc README.rst CHANGES.rst
%license docs/COPYING
%{python2_sitearch}/PIL/
%{python2_sitearch}/Pillow-%{version}-py2.7.egg-info/


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Sandro Mani <manisandro@gmail.com> - 6.2.2-1
- Update to 6.2.2

* Sat Jan 04 2020 Sandro Mani <manisandro@gmail.com> - 6.2.1-2
- Add full description
- %%{python2_sitearch}/* -> %%{python2_sitearch}/PIL/
- Remove files instead of using %%exclude
- Don't provide python-imaging

* Sat Jan 04 2020 Sandro Mani <manisandro@gmail.com> - 6.2.1-1
- Minimal python2-only package
