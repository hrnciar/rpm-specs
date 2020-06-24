Name:          gtkspellmm30
Version:       3.0.5
Release:       11%{?dist}
License:       GPLv2+
Summary:       On-the-fly spell checking for GtkTextView widgets - C++ bindings
URL:           http://gtkspell.sourceforge.net/
Source0:       http://sourceforge.net/projects/gtkspell/files/gtkspellmm/gtkspellmm-%{version}.tar.xz

BuildRequires: gcc-c++
BuildRequires: gtkspell3-devel
BuildRequires: gtkmm30-devel
BuildRequires: gtkmm30-doc
BuildRequires: make

%description
GtkSpell provides word-processor-style highlighting and replacement of
misspelled words in a GtkTextView widget as you type. Right-clicking a
misspelled word pops up a menu of suggested replacements.

%package       devel
Summary:       Development files for gtkspellmm30
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description   devel
The gtkspellmm30-devel package provides header and documentation files for
developing C++ applications which use GtkSpell.

%package       doc
Summary:       Documentation for %{name}
BuildArch:     noarch
Requires:      gtkmm30-doc

%description   doc
This package contains the full API documentation for %{name}.


%prep
%autosetup -n gtkspellmm-%{version}


%build
%if 0%{?fedora} == 23
export CFLAGS="%optflags -std=c++11"
export CXXFLAGS="%optflags -std=c++11"
%endif
%configure

%make_build


%install
%make_install
find %{buildroot} -name "*.la" -exec rm {} \;


%ldconfig_scriptlets


%files
%doc AUTHORS ChangeLog NEWS README
%license COPYING
%{_libdir}/libgtkspellmm-3.0.so.0*

%files devel
%{_includedir}/gtkspellmm-3.0
%{_libdir}/libgtkspellmm-3.0.so
%{_libdir}/pkgconfig/gtkspellmm-3.0.pc
%{_libdir}/gtkspellmm-3.0

%files doc
%license COPYING
%{_datadir}/devhelp/books/gtkspellmm-3.0
%{_datadir}/doc/gtkspellmm-3.0

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 14 2018 Sandro Mani <manisandro@gmail.com> - 3.0.5-8
- Rebuild (gtkspell3)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Feb 18 2018 Sandro Mani <manisandro@gmail.com> - 3.0.5-6
- Add missing BR: gcc-c++, make

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Aug 08 2016 Sandro Mani <manisandro@gmail.com> - 3.0.5-1
- Update to 3.0.5

* Tue Apr 05 2016 Sandro Mani <manisandro@gmail.com> - 3.0.4-2
- Respin

* Sun Apr 03 2016 Sandro Mani <manisandro@gmail.com> - 3.0.4-1
- Update to 3.0.4

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 3.0.3-5
- Rebuilt for GCC 5 C++11 ABI change

* Fri Mar 06 2015 Sandro Mani <manisandro@gmail.com> - 3.0.3-4
- Rebuild for GCC5 ABI change
- Modernize spec file

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr 30 2014 Sandro Mani <manisandro@gmail.com> - 3.0.3-1
- Update to 3.0.3

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jun 04 2013 Sandro Mani <manisandro@gmail.com> - 3.0.2-1
- Update to 3.0.2

* Fri Apr 26 2013 Sandro Mani <manisandro@gmail.com> - 3.0.1-1
- New upstream release (uses correct GPLv2 license headers)

* Fri Mar 08 2013 Sandro Mani <manisandro@gmail.com> - 3.0.0-1
- Initial package.
