Name:           amftools
Version:        0.0
%global         svn svn32
%global         snapshot 20121220%{svn}
Release:        20.%{snapshot}%{?dist}
Summary:        AMF file library
# License is in files
License:        LGPLv3+
URL:            https://sourceforge.net/projects/%{name}/
# svn export svn://svn.code.sf.net/p/%%{name}/code/trunk %%{name}
# tar -pczf %%{name}-%%{svn}.tar.gz %%{name}
Source0:        %{name}-%{svn}.tar.gz
Source1:        %{name}-Makefile
BuildRequires:  mesa-libGL-devel, libzip-devel, muParser-devel, stbi-devel, rapidxml-devel, gcc-c++

%description
C++ tools for implementing AMF file format for the interchange of geometry
for 3D printing (additive manufacturing).

%package devel
Summary: AMF tools development files
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for AMF tools.

%prep
%setup -qn %{name}
cp %{SOURCE1} Makefile

# Bundling
rm -rf */muparser */stb_image include/rapidxml */zip
sed -i 's|muparser/muParser.h|muParser.h|g' include/Equation.h
sed -i 's|stb_image/stb_image.h|stb_image.h|g' src/SimpleImage.cpp
sed -i 's|rapidxml/||g' include/XmlStream.h src/XmlStream.cpp

%build
make %{?_smp_mflags}

%install
install -Dpm0755 libamf.so.0.0 %{buildroot}%{_libdir}/libamf.so.0.0
ln -s libamf.so.0.0 %{buildroot}%{_libdir}/libamf.so.0
ln -s libamf.so.0.0 %{buildroot}%{_libdir}/libamf.so
mkdir -p %{buildroot}%{_includedir}
cp -arp include %{buildroot}%{_includedir}/amf

%files
%{_libdir}/libamf.so.*

%files devel
%{_libdir}/libamf.so
%{_includedir}/amf

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-20.20121220svn32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-19.20121220svn32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-18.20121220svn32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-17.20121220svn32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-16.20121220svn32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-15.20121220svn32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-14.20121220svn32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0-13.20121220svn32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Tue Feb 28 2017 Remi Collet <remi@fedoraproject.org> - 0.0-12.20121220svn32
- rebuild for new libzip

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-11.20121220svn32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-10.20121220svn32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0-9.20121220svn32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 06 2015 Remi Collet <remi@fedoraproject.org> - 0.0-8.20121220svn32
- rebuild for new libzip

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.0-7.20121220svn32
- Rebuilt for GCC 5 C++11 ABI change

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0-6.20121220svn32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0-5.20121220svn32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Aug 21 2013 Remi Collet <rcollet@redhat.com> - 0.0-4.20121220svn32
- rebuild for new libzip

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0-3.20121220svn32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Apr 24 2013 Miro Hrončok <mhroncok@redhat.com> - 0.0-2.20121220svn32
- Soname version 0.0.0 -> 0.0
- Removing include/zip in %%prep, as it works fine
- Added -lmuparser to Makefile

* Fri Feb 01 2013 Miro Hrončok <mhroncok@redhat.com> - 0.0-1.20121220svn32
- Started

