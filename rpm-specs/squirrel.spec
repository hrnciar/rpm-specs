Name:           squirrel
Version:        2.2.5
Release:        20%{?dist}
Summary:        High level imperative/OO programming language

License:        zlib
URL:            http://squirrel-lang.org/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}_%{version}_stable.tar.gz
Patch0:         squirrel-autotools.patch
Patch1:         squirrel-2.2.4-mem.patch

BuildRequires:  gcc-c++
BuildRequires:  libtool

%description
Squirrel is a high level imperative/OO programming language, designed
to be a powerful scripting tool that fits in the size, memory bandwidth,
and real-time requirements of applications like games.

%package libs
Summary:        Libraries needed to run Squirrel scripts

%description libs
Libraries needed to run Squirrel scripts.

%package devel
Summary:        Development files needed to use Squirrel libraries
Requires:       %{name}-libs = %{version}-%{release}

%description devel
Development files needed to use Squirrel libraries.


%prep
%setup -q -c

# fix file permissions
find . -type f -exec chmod a-x {} \;

pushd SQUIRREL2
%patch0 -p1 -b .autotools
%patch1 -p1 -b .mem

# fix extension for autotools
mv sq/sq.c sq/sq.cpp

# fix EOL + preserve timestamps
for f in README HISTORY COPYRIGHT
do
    sed -i.orig 's/\r//g' $f
    touch -r $f.orig $f
done

sh autogen.sh
popd


%build
export CXXFLAGS="-std=c++14 $RPM_OPT_FLAGS"
pushd SQUIRREL2
%configure --disable-static
make %{?_smp_mflags}
popd


%install
pushd SQUIRREL2
make DESTDIR=$RPM_BUILD_ROOT INSTALL="/usr/bin/install -p" install
popd

rm $RPM_BUILD_ROOT%{_libdir}/*.la


%files
%doc SQUIRREL2/{README,HISTORY,COPYRIGHT}
%{_bindir}/sq

%files libs
%doc SQUIRREL2/COPYRIGHT
%{_libdir}/libsqstdlib-%{version}.so
%{_libdir}/libsquirrel-%{version}.so

%files devel
%doc SQUIRREL2/doc/*.pdf
%{_includedir}/squirrel
%{_libdir}/pkgconfig/squirrel.pc
%{_libdir}/libsqstdlib.so
%{_libdir}/libsquirrel.so


%changelog
* Tue Oct 06 2020 Jeff Law <law@redhat.com> - 2.2.5-20
- Force C++14 as this code is not C++17 ready

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.2.5-8
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Apr 20 2014 Dan Horák <dan[at]danny.cz> - 2.2.5-5
- spec cleanup

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Dan Horák <dan[at]danny.cz> - 2.2.5-1
- update to upstream version 2.2.5
- fix build with gcc 4.7

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Dec 27 2009 Dan Horák <dan[at]danny.cz> 2.2.4-1
- update to upstream version 2.2.4

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul  1 2009 Dan Horák <dan[at]danny.cz> 2.2.3-1
- update to upstream version 2.2.3

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Oct 13 2008 Dan Horák <dan[at]danny.cz> 2.2.2-1
- update to upstream version 2.2.2

* Sat May 31 2008 Dan Horak <dan[at]danny.cz> 2.2.1-1
- update to upstream version 2.2.1
- update URL of Source0
- really preserve timestamps on modified files

* Sun Apr 27 2008 Dan Horak <dan[at]danny.cz> 2.2-2
- enable parallel make
- add missing %%defattr for subpackages
- preserve timestamps

* Sun Apr 13 2008 Dan Horak <dan[at]danny.cz> 2.2-1
- initial version 2.2
