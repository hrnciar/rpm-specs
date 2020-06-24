# This package depends on automagic byte compilation
# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_2
%global _python_bytecompile_extra 1

%global __python %{__python3}

Name:           gnome-code-assistance
Version:        3.16.1
Release:        17%{?dist}
Summary:        Common code assistance services for code editors

License:        GPLv3+
URL:            http://wiki.gnome.org/Projects/CodeAssistance

Source0:        https://download.gnome.org/sources/%{name}/3.16/%{name}-%{version}.tar.xz

# vala 0.36 support, backported from upstream
Patch0:         gnome-code-assistance-vala-0.36.patch

BuildArch:      noarch

BuildRequires:  libtool
BuildRequires:  gcc

# C Backend
BuildRequires:  clang-devel
BuildRequires:  llvm-devel

# Python and XML backends:
BuildRequires:  python3
BuildRequires:  python3-dbus
BuildRequires:  python3-gobject
BuildRequires:  python3-lxml
BuildRequires:  python3-simplejson
BuildRequires:  python3-devel
# Javascript Backend:
BuildRequires:  gjs

# Vala backend:
BuildRequires:  vala-devel
BuildRequires:  libgee-devel

#Ruby/CSS/ Backend:
BuildRequires:  ruby
BuildRequires:  rubygem-ruby-dbus
BuildRequires:  rubygem-sass

# For patch0
BuildRequires:  autoconf automake

Requires:  ruby
Requires:  rubygem-ruby-dbus
Requires:  rubygem-sass
Requires:  gjs
Requires:  python3
Requires:  python3-lxml
Requires:  python3-dbus
Requires:  python3-gobject
Requires:  python3-simplejson
Requires:  clang
Requires:  dbus

%description
gnome-code-assistance is a project which aims to provide common code assistance
services for code editors (simple editors as well as IDEs). It is an effort to
provide a centralized code-assistance as a service for the GNOME platform
instead of having every editor implement their own solution.

%prep
%autosetup -p1


%build
# For patch0
autoreconf -fi

%configure --disable-static --disable-silent-rules --disable-vala
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%files
%license COPYING
%doc README NEWS
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/*
%{_datadir}/glib-2.0/schemas/org.gnome.codeassistance.gschema.xml
%{_datadir}/dbus-1/services/*.service

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.16.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.16.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Apr 04 2019 Kalev Lember <klember@redhat.com> - 3.16.1-15
- Disable vala backend

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.16.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Aug 06 2018 Kalev Lember <klember@redhat.com> - 3.16.1-13
- Rebuilt for vala 0.42

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.16.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.16.1-11
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.16.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Dec 20 2017 Kalev Lember <klember@redhat.com> - 3.16.1-9
- Rebuilt for vala 0.40

* Mon Aug 21 2017 Kalev Lember <klember@redhat.com> - 3.16.1-8
- Rebuilt for vala 0.38

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.16.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.16.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 13 2017 Kalev Lember <klember@redhat.com> - 3.16.1-5
- Rebuilt for vala 0.36

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.16.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 3.16.1-3
- Rebuild for Python 3.6

* Thu Sep 22 2016 Kalev Lember <klember@redhat.com> - 3.16.1-2
- Rebuilt for vala 0.34

* Tue Jul 05 2016 Kalev Lember <klember@redhat.com> - 3.16.1-1
- Update to 3.16.1

* Mon Mar 07 2016 Kalev Lember <klember@redhat.com> - 3.16.0-6
- Rebuilt for vala 0.32

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.16.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.16.0-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.16.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 27 2015 Kalev Lember <kalevlember@gmail.com> - 3.16.0-2
- Rebuilt for vala 0.30

* Wed Apr 29 2015 Kalev Lember <kalevlember@gmail.com> - 3.16.0-1
- Update to 3.16.0
- Use license macro for the COPYING file

* Wed Feb 25 2015 Ville Skyttä <ville.skytta@iki.fi> - 3.14.0-3
- Apply upstream fix to actually build with vala 0.28
- Make build more verbose, use %%autosetup

* Sat Feb 21 2015 Kalev Lember <kalevlember@gmail.com> - 3.14.0-2
- Rebuilt for vala 0.28

* Thu Dec 04 2014 Kalev Lember <kalevlember@gmail.com> - 3.14.0-1
- Update to 3.14.0

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jul 23 2014 Kalev Lember <kalevlember@gmail.com> - 0.3.1-7
- Rebuilt for vala 0.26

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 06 2014 Elad Alfassa <elad@fedoraproject.org> - 0.3.1-5
- Fix unowned directory
- Require python3-devel as per packaging guidelines
- Make sure we only compile python3 bytecode

* Mon May 05 2014 Elad Alfassa <elad@fedoraproject.org> - 0.3.1-4
- BuildRequire python3-simplejson so it's not bundled

* Mon May 05 2014 Elad Alfassa <elad@fedoraproject.org> - 0.3.1-3
- BuildRequire rubygem-sass so it's not bundled
- Fix up license tag

* Tue Apr 22 2014 Elad Alfassa <elad@fedoraproject.org> - 0.3.1-2
- Address issues from review

* Fri Apr 04 2014 Elad Alfassa <elad@fedoraproject.org> - 0.3.1-1
- Update to upstream 0.3.1

* Mon Mar  3 2014 Elad Alfassa <elad@fedoraproject.org>
- Initial Build
