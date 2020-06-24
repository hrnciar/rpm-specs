%ifarch x86_64 i686
%bcond_without ddcpci
%else
%bcond_with ddcpci
%endif

#%%global git_commit 811d34d95f5740ae8310dba3521155ad0f70fc0c
#%%global git_date 20170623

#%%global git_short_commit %%(c=%%{git_commit}; echo ${c:0:8})
#%%global git_suffix %%{git_date}git%%{git_short_commit}

Name:             ddccontrol
#URL:              http://ddccontrol.sourceforge.net/
URL:              https://github.com/ddccontrol/ddccontrol
Version:          0.4.4
Release:          3%{?dist}
License:          GPLv2+
BuildRequires:    gtk2-devel, pkgconfig, pciutils-devel, desktop-file-utils
BuildRequires:    perl(XML::Parser), gettext, libtool, libxml2-devel, tidy
BuildRequires:    libX11-devel, xml-common, libxslt, libXt-devel
BuildRequires:    docbook-style-xsl, gettext-devel, intltool
Requires:         ddccontrol-db, /sbin/modprobe
Requires(post):   /sbin/modprobe
Summary:          Control your monitor by software using the DDC/CI protocol
Source0:          https://github.com/ddccontrol/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# autoload i2c-dev module
Source1:          %{name}-modules-autoload.conf
# no monitors on s390(x)
ExcludeArch:      s390 s390x

%description
DDCcontrol is a program to control monitor parameters, like brightness and
contrast, by software, i.e. without using the OSD (On Screen Display) and
the monitor HW controls.

%package gtk
Summary:        GTK GUI for ddccontrol
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       hicolor-icon-theme

%description gtk
This package provides the GTK graphical user interface for ddccontrol.

%package doc
Summary:        Documentation files for ddccontrol
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description doc
Documentation files for ddccontrol.

%package devel
Summary:        Development files for ddccontrol
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for ddccontrol.

%prep
%setup -q

%build
./autogen.sh

# workaround for GCC-10, problem reported upstream
export CFLAGS="%{optflags} -fcommon"

# applet is not supported on Gnome 3
%configure --enable-doc --disable-gnome-applet --prefix=%{_prefix} \
  --exec-prefix=%{_exec_prefix} --disable-rpath %{!?with_ddcpci:--disable-ddcpci}

# kill rpaths
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

# use as-needed to remove unused-direct-shlib-dependency
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool

make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} libdir=%{_libdir}

desktop-file-validate %{buildroot}%{_datadir}/applications/gddccontrol.desktop

# autoload i2c-dev module
install -m 644 -D %{SOURCE1} %{buildroot}%{_prefix}/lib/modules-load.d/%{name}.conf

# move html to subdir
mkdir %{buildroot}%{_docdir}/%{name}/html
mv %{buildroot}%{_docdir}/%{name}/*.html %{buildroot}%{_docdir}/%{name}/html

# remove static and *.la files
rm -f %{buildroot}%{_libdir}/{*.a,*.la}

# remove Bluecurve icon (duplicate of the hicolor one)
rm -rf %{buildroot}%{_datadir}/icons/Bluecurve

%find_lang %{name}

%post
# autoload i2c-dev module
/sbin/modprobe i2c-dev &>/dev/null || :

%files -f %{name}.lang
%license COPYING
%doc AUTHORS NEWS README.md TODO
%exclude %{_docdir}/%{name}/html
%{_bindir}/ddccontrol
%if 0%{?with_ddcpci}
%{_libexecdir}/%{name}/ddcpci
%endif
%{_prefix}/lib/modules-load.d/%{name}.conf
%{_libdir}/lib*.so.*
%{_mandir}/man1/ddccontrol.1*

%files gtk
%{_bindir}/gddccontrol
%{_mandir}/man1/gddccontrol.1*
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/applications/*

%files doc
%doc %{_docdir}/%{name}/html

%files devel
%{_includedir}/%{name}
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Mon Feb 10 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 0.4.4-3
- Fixed FTBFS with gcc-10
  Resolves: rhbz#1799275

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Oct 21 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 0.4.4-1
- New version
- Dropped gcc10-compile-fix patch (already in upstream)

* Mon Oct 21 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 0.4.3-8
- Fixed compilation with gcc-10
- Called autogen.sh in build phase

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.3-3
- Remove obsolete scriptlets

* Tue Jan  2 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 0.4.3-2
- Fixed URL

* Tue Jan  2 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 0.4.3-1
- New version

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-18.20170623git811d34d9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-17.20170623git811d34d9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 23 2017 Jaroslav Škarvada <jskarvad@redhat.com> - 0.4.2-16.20170623git811d34d9
- New snapshot
- New source URL (GitHub)
- Dropped autopoint patch (not needed)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-15.20120904gitc3af663d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Mar 18 2016 Jaroslav Škarvada <jskarvad@redhat.com> - 0.4.2-14.20120904gitc3af663d
- Added modprobe to requires

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-13.20120904gitc3af663d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-12.20120904gitc3af663d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Dec 16 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 0.4.2-11.20120904gitc3af663d
- Conditionalized ddcpci build, it is build only on i686, x86_64 architectures
- Fixed icons packaging

* Wed Dec 10 2014 David King <amigadave@amigadave.com> - 0.4.2-10.20120904gitc3af663d
- Fix directory ownership for icons and pkg-config (#1172555)

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-9.20120904gitc3af663d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-8.20120904gitc3af663d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Aug  6 2013 Jaroslav Škarvada <jskarvad@redhat.com> - 0.4.2-7.20120904gitc3af663d
- Used unversioned doc directory
  Resolves: rhbz#993720

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-6.20120904gitc3af663d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-5.20120904gitc3af663d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Sep 18 2012 Dan Horák <dan[at]danny.cz> - 0.4.2-4.20120904gitc3af663d
- no monitors on s390(x)

* Tue Sep 04 2012 Jaroslav Škarvada <jskarvad@redhat.com> - 0.4.2-3.20120904gitc3af663d
- Rebased to latest git head

* Tue Sep 04 2012 Jaroslav Škarvada <jskarvad@redhat.com> - 0.4.2-2
- Desktop file and icon moved to gtk subpackage
- Man pages are no longer explicitly gzipped
- Config for modules autoload moved to /usr/lib/modules-load.d
- Fixed requirements for gtk subpackage
- Fixed unused-direct-shlib-dependency

* Wed Aug 29 2012 Jaroslav Škarvada <jskarvad@redhat.com> - 0.4.2-1
- Initial version
