%global debug_package %{nil}
%global _docdir_fmt %{name}

Name:           notify-sharp3
Version:        3.0.3
Release:        12%{?dist}
Summary:        A C# implementation for Desktop Notifications

License:        MIT
URL:            https://www.meebey.net/projects/notify-sharp
Source0:        https://www.meebey.net/projects/notify-sharp/downloads/notify-sharp-%{version}.tar.gz

BuildRequires:  mono-devel, gtk-sharp3-devel, gnome-sharp-devel, dbus-sharp-glib-devel
BuildRequires:  autoconf, automake, libtool

BuildRequires:  monodoc-devel
# Mono only available on these:
ExclusiveArch: %{mono_arches}

%description
notify-sharp is a C# client implementation for Desktop Notifications,
i.e. notification-daemon. It is inspired by the libnotify API.

Desktop Notifications provide a standard way of doing passive pop-up
notifications on the Linux desktop. These are designed to notify the
user of something without interrupting their work with a dialog box
that they must close. Passive pop-ups can automatically disappear after
a short period of time.

%package devel
Summary:        Development files for notify-sharp
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description devel
Development files for notify-sharp

%package doc
Summary:        Documentation files for notify-sharp
Requires:       %{name} = %{version}-%{release}
Requires:       monodoc
BuildArch:      noarch

%description doc
Documentation files for notify-sharp

%prep
%setup -qn notify-sharp-%{version}

%build
sed -i "s#dbus-sharp-1.0#dbus-sharp-2.0#g" configure.ac
sed -i "s#dbus-sharp-glib-1.0#dbus-sharp-glib-2.0#g" configure.ac
sed -i "s#gmcs#mcs#g" configure.ac
autoreconf --install
%configure --libdir=%{_prefix}/lib --disable-docs
make %{?_smp_mflags}

%install
%make_install

mkdir -p $RPM_BUILD_ROOT%{_libdir}/pkgconfig/
test "%{_libdir}" = "%{_prefix}/lib" || mv $RPM_BUILD_ROOT%{_prefix}/lib/pkgconfig/*.pc $RPM_BUILD_ROOT%{_libdir}/pkgconfig/

%files
%doc NEWS README AUTHORS
%license COPYING
%{_monogacdir}/notify-sharp/
%{_monodir}/notify-sharp*/

%files devel
%{_libdir}/pkgconfig/notify-sharp*.pc

%files doc

%changelog
* Mon Feb 03 2020 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 3.0.3-12
- built without docs because mdoc.exe is not built with Mono 6 and mcs anymore

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Mar 02 2017 Claudio Rodrigo Pereyra Diaz <elsupergomez@fedoraproject.org> - 3.0.3-4
- Rebuilt for new dbus-sharp

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Oct 13 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.3-2
- mono rebuild for aarch64 support

* Mon Apr 20 2015 Claudio Rodrigo Pereyra Diaz <elsupergomez@fedoraproject.org> - 3.0.3-1
- Packaging version 3
