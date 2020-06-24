%global gauche_main_version 0.97


Name:           gauche-gl
Version:        0.6
Release:        15%{?dist}
Summary:        OpenGL binding for Gauche

License:        BSD
URL:            http://practical-scheme.net/
Source:         http://practical-scheme.net/vault/Gauche-gl-%{version}.tgz

BuildRequires:  gcc
BuildRequires:  gauche-devel
BuildRequires:  freeglut-devel
BuildRequires:  libSM-devel
BuildRequires:  libXext-devel
BuildRequires:  libXi-devel
BuildRequires:  libXmu-devel
BuildRequires:  texinfo


%description
OpenGL binding for Gauche.


%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for %{name}.


%prep
%autosetup -n Gauche-gl-%{version}
# add RPM opt flags
sed -i 's/@X_CFLAGS@/@X_CFLAGS@ @CFLAGS@/g' src/Makefile.in


%build
%configure
make %{?_smp_mflags}


%install
%if 0%{?el5}
rm -rf $RPM_BUILD_ROOT
%endif
make install DESTDIR=$RPM_BUILD_ROOT

# no japanese info docs
rm -f $RPM_BUILD_ROOT%{_infodir}/gauche-gl-refj.*

# make .so files executable
find $RPM_BUILD_ROOT -name '*.so' -exec chmod 0755 '{}' ';'

# include file not necessary
rm -rf $RPM_BUILD_ROOT%{_libdir}/gauche/%{gauche_version}*/include

# correct end-of-line-encoding
sed -i 's/\r//' examples/slbook/ogl2particle/* examples/slbook/ogl2brick/*

# these are not necessary
rm -f examples/glbook/run
rm -f examples/slbook/ogl2particle/run.sh

# set read permissions for debuginfo package
find . -print0 | xargs -0 chmod a+r


%check
make check

%files
%doc examples
%license COPYING
%{_libdir}/gauche-%{gauche_main_version}/site/*/libgauche-*.so
%{_datadir}/gauche-%{gauche_main_version}/site/lib/.packages/Gauche-gl.gpd
%{_datadir}/gauche-%{gauche_main_version}/site/lib/gl.scm
%{_datadir}/gauche-%{gauche_main_version}/site/lib/gl
%{_infodir}/gauche-gl-refe.*


%files devel
%{_libdir}/gauche-%{gauche_main_version}/site/include/gauche/math3d.h


%changelog
* Fri Apr  3 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.6-15
- Rebuilt for Gauche 0.9.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 03 2019 Björn Esser <besser82@fedoraproject.org> - 0.6-11
- Remove versioned BR on gauche-devel, fixes FTBFS (#1604052)
- Add BuildRequires: gcc
- Use %%license for COPYING file

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 0.6-8
- Rebuilt for switch to libxcrypt

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May  4 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.6-2
- Drop ExcludeArch for ppc64

* Thu Dec  4 2014 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.6-1
- Update to 0.6

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun May 13 2012 Michel Salim <salimma@fedoraproject.org> - 0.5.1-4
- Rebuild for Gauche 0.9.3.x
- Spec clean-ups

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Sep 15 2011 Michel Salim <salimma@fedoraproject.org> - 0.5.1-2
- Put header in -devel subpackage
- Fix overlapping directory ownerships

* Thu Sep 15 2011 Michel Salim <salimma@fedoraproject.org> - 0.5.1-1
- Update to 0.5.1

* Mon Feb 14 2011 Gérard Milmeister <gemi@bluewin.ch> - 0.5-1
- new release 0.5 matching gauche 0.9

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jun 20 2009 Gerard Milmeister <gemi@bluewin.ch> - 0.4.4-5
- updated for gauche 0.8.14

* Thu Feb 14 2008 Gerard Milmeister <gemi@bluewin.ch> - 0.4.4-3
- rebuild for gauche 0.8.13

* Sat Aug 18 2007 Gerard Milmeister <gemi@bluewin.ch> - 0.4.4-2
- exclude arch ppc64, depends on non-existing ppc64 gauche

* Sat Aug 18 2007 Gerard Milmeister <gemi@bluewin.ch> - 0.4.4-1
- new release 0.4.4

* Fri Apr 20 2007 Gerard Milmeister <gemi@bluewin.ch> - 0.4.3-3
- rebuild for gauche 0.8.10

* Thu Feb 22 2007 Gerard Milmeister <gemi@bluewin.ch> - 0.4.3-2
- added patch for compiling with opt flags

* Thu Jan 18 2007 Gerard Milmeister <gemi@bluewin.ch> - 0.4.3-1
- new version 0.4.3

* Mon Nov 13 2006 Gerard Milmeister <gemi@bluewin.ch> - 0.4.2-1
- new version 0.4.2

* Fri May  5 2006 Gerard Milmeister <gemi@bluewin.ch> - 0.4.1-4
- cleaned up Requires
- removed unnecessary files

* Sun Nov  6 2005 Gerard Milmeister <gemi@bluewin.ch> - 0.4.1-1
- New Version 0.4.1

* Fri Jul  1 2005 Gerard Milmeister <gemi@bluewin.ch> - 0.4-1
- New Version 0.4

* Wed Feb 23 2005 Gerard Milmeister <gemi@bluewin.ch> - 0:0.3.1-1
- New Version 0.3.1

* Mon Nov 10 2003 Gerard Milmeister <gemi@bluewin.ch> - 0:0.3-0.fdr.1
- First Fedora release

