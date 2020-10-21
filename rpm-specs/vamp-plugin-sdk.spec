Name:           vamp-plugin-sdk
Version:        2.9.0
Release:        2%{?dist}
Summary:        An API for audio analysis and feature extraction plugins

License:        BSD
URL:            https://vamp-plugins.org/
Source0:        https://code.soundsoftware.ac.uk/attachments/download/2588/%{name}-%{version}.tar.gz
Patch0:         %{name}-2.9.0-libdir.patch

BuildRequires:  gcc-c++
BuildRequires:  libsndfile-devel
#Requires:

%description
Vamp is an API for C and C++ plugins that process sampled audio data
to produce descriptive output (measurements or semantic observations).

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        static
Summary:        Static libraries for %{name}
Requires:       %{name}-devel = %{version}-%{release}

%description    static
The %{name}-static package contains library files for
developing static applications that use %{name}.


%prep
%autosetup -p1
sed -i 's|/lib/vamp|/%{_lib}/vamp|g' src/vamp-hostsdk/PluginHostAdapter.cpp
sed -i 's|/lib/|/%{_lib}/|g' src/vamp-hostsdk/PluginLoader.cpp


%build
%configure
%make_build


%install
# fix libdir
find . -name '*.pc.in' -exec sed -i 's|/lib|/%{_lib}|' {} ';'
%make_install

find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

# create Makefile for examples
cd examples
echo CXXFLAGS=$RPM_OPT_FLAGS -fpic >> Makefile-%{_arch}
echo bundle: `ls *.o` >> Makefile
echo -e "\t"g++ \$\(CXXFLAGS\) -shared -Wl,-Bsymbolic \
     -o vamp-example-plugins.so \
     *.o \$\(pkg-config --libs vamp-sdk\) >> Makefile
echo `ls *.cpp`: >> Makefile
echo -e "\t"g++ \$\(CXXFLAGS\) -c $*.cpp >> Makefile
echo clean: >> Makefile
echo -e "\t"-rm *.o *.so >> Makefile
# clean directory up so we can package the sources
make clean


%check
# Scan shared libs for unpatched '/lib' strings to prevent issues
# on 64-bit multilib platforms.
[ $(strings ${RPM_BUILD_ROOT}%{_libdir}/lib*.so.?|grep /lib/|sed -e 's!/%{_lib}!/__FEDORA-LIB__!g'|grep -c /lib/) -eq 0 ]


%ldconfig_scriptlets


%files
%license COPYING
%doc README
%{_libdir}/*.so.*
%{_libdir}/vamp

%files devel
%doc examples
%{_bindir}/vamp-*
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%files static
%{_libdir}/*.a


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Feb  2 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 2.9.0-1
- Update to 2.9.0

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul  1 2019 Michel Alexandre Salim <salimma@fedoraproject.org> - 2.8.0-1
- Update to 2.8.0

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Michel Alexandre Salim <salimma@fedoraproject.org> - 2.7.1-1
- Update to 2.7.1

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Apr 27 2015 Nils Philippsen <nils@redhat.com> - 2.5-6
- Rebuild for gcc 5.1.0 C++ ABI change

* Wed Apr 1 2015 Orion Poplawski <orion@cora.nwra.com> - 2.5-5
- Rebuild for gcc 5.0.0 C++ ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jun 18 2013 Michel Salim <salimma@fedoraproject.org> - 2.5-1
- Update to 2.5

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Sep  9 2012 Michel Salim <salimma@fedoraproject.org> - 2.4-1
- Update to 2.4

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-3
- Rebuilt for c++ ABI breakage

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 14 2011 Michel Salim <salimma@fedoraproject.org> - 2.2.1-1
- Update to 2.2.1

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri May 28 2010 Michel Salim <salimma@fedoraproject.org> - 2.1-1
- Update to 2.1
- multilib fix: Makefile for examples is now arch-tagged

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Mar 31 2009 Michael Schwendt <mschwendt@fedoraproject.org> - 2.0-5
- Add another sed libdir fix for PluginLoader.cpp (#469777)
  plus a check section to scan for libdir issues

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Feb  8 2009 Michel Salim <salimma@fedoraproject.org> - 2.0-3
- Fix compilation problem with GCC 4.4

* Tue Dec 30 2008 Michel Salim <salimma@fedoraproject.org> - 2.0-2
- More libdir fixes (bug #469777)

* Sun Dec 14 2008 Michel Salim <salimma@fedoraproject.org> - 2.0-1
- Update to 2.0

* Thu Jul 17 2008 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.3-1
- Update to 1.3

* Thu Jan 31 2008 Michel Salim <michel.sylvan@gmail.com> - 1.1b-4
- Add some #includes, needed due to GCC 4.3's header dependency cleanup

* Mon Jan 28 2008 Michel Salim <michel.sylvan@gmail.com> - 1.1b-3
- Add examples to -devel subpackage
- Fix .pc files
- Preserve timestamps when installing

* Sun Jan 27 2008 Michel Salim <michel.sylvan@gmail.com> - 1.1b-2
- Add missing build requirement on libsndfile-devel

* Wed Jan 16 2008 Michel Salim <michel.sylvan@gmail.com> - 1.1b-1
- Initial Fedora package
