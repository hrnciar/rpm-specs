%undefine _hardened_build

Name:    sugar-toolkit-gtk3
Version: 0.116
Release: 10%{?dist}
Summary: Sugar toolkit GTK+ 3
License: LGPLv2+
URL:     http://wiki.laptop.org/go/Sugar

Source0: http://download.sugarlabs.org/sources/sucrose/glucose/%{name}/%{name}-%{version}.tar.xz
Source1: macros.sugar
Patch0:  Build-by-default-for-python-3.patch
Patch1:  fix-RuntimeError-could-not-create-signal-for-closing.patch
Patch2:  fix-sugar-install-bundle.patch
Patch3:  use-xml.etree.ElementTree.patch

BuildRequires: alsa-lib-devel
BuildRequires: gettext-devel
BuildRequires: gtk3-devel
BuildRequires: gobject-introspection-devel
BuildRequires: intltool
BuildRequires: librsvg2-devel
BuildRequires: libSM-devel
BuildRequires: perl-XML-Parser
BuildRequires: pkgconfig
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: pygobject3-devel
Requires: python3-dateutil
Requires: python3-dbus
Requires: python3-gobject
Requires: gettext
Requires: sugar-datastore
Requires: unzip
Requires: webkit2gtk3

%description
Sugar is the core of the OLPC Human Interface. The toolkit provides
a set of widgets to build HIG compliant applications and interfaces
to interact with system services like presence and the datastore.
This is the toolkit depending on GTK3.

%package devel
Summary: Invokation information for accessing SugarExt-1.0
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the invocation information for accessing
the SugarExt-1.0 library through gobject-introspection.

%prep
%autosetup -p1

%build
%configure
# There are missing dependencies in this project's Makefiles, in
# particular dependencies on libsugarext.   LTO is tripping these
# issues regularly.
make -O V=1 VERBOSE=1

%install
%make_install

mkdir -p %{buildroot}/%{_rpmconfigdir}/macros.d/
install -pm 644 %{SOURCE1} %{buildroot}/%{_rpmconfigdir}/macros.d/macros.sugar

%find_lang %name

#Remove libtool archives.
find %{buildroot} -type f -name "*.la" -delete

%ldconfig_scriptlets

%files -f %{name}.lang
%license COPYING
%exclude %{_bindir}/sugar-activity
%{_bindir}/sugar-activity3
%{python3_sitelib}/*
%{_bindir}/sugar-activity-web
%{_rpmconfigdir}/macros.d/macros.sugar
%{_libdir}/girepository-1.0/*.typelib
%{_libdir}/lib*.so.*

%files devel
%{_libdir}/*.so
%{_datadir}/gir-1.0/*.gir

%changelog
* Tue May 26 2020 Jeff Law <law@redhat.org> - 0.116-10
- Disable parallel builds due to missing Makefile dependencies

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.116-10
- Rebuilt for Python 3.9

* Sun May 10 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.116-9
- Add patch to fix use of xml.etree.ElementTree

* Sat May 2 2020 Ibiam Chihurumnaya <ibiamchihurumnaya@gmail.com> 0.116-8
- Add upstream patch to fix sugar-install bundle

* Mon Mar 2 2020 Ibiam Chihurumnaya <ibiamchihurumnaya@gmail.com> 0.116-7
- Add upstream patch to build for python3 by default

* Sun Feb 2 2020 Peter Robinson <pbrobinson@fedoraproject.org> 0.116-6
- Add upstream patch to fix runtime error signal crash

* Sat Feb  1 2020 Peter Robinson <pbrobinson@fedoraproject.org> 0.116-5
- Re-add hardened disable

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.116-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 27 2020 Peter Robinson <pbrobinson@fedoraproject.org> 0.116-3
- Drop support for running legacy python2 activities

* Sat Jan 25 2020 Peter Robinson <pbrobinson@fedoraproject.org> 0.116-2
- Update for python3 builds

* Fri Jan 24 2020 Chihurumnaya Ibiam <ibiamchihurumnaya@gmail.com> 0.116-1
- Update to 0.116 release

* Wed Aug 28 2019 Peter Robinson <pbrobinson@fedoraproject.org> 0.114-1
- Update to 0.114 release

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.113-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Apr 21 2019 Miro Hrončok <mhroncok@redhat.com> - 0.113-2
- Update Python requirements to be single version

* Tue Apr 16 2019 Peter Robinson <pbrobinson@fedoraproject.org> 0.113-1
- Update to sugar 0.113 release

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.112-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Sep 20 2018 Peter Robinson <pbrobinson@fedoraproject.org> 0.112-6
- Minor cleanups

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.112-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.112-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Feb 01 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.112-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Jan 12 2018 Tomas Popela <tpopela@redhat.com> - 0.112-2
- Adapt to the webkitgtk4 rename
