%global module_name ibus_cangjie

Name:             ibus-cangjie
Summary:          IBus engine to input Cangjie and Quick
Version:          2.4
Release:          20%{?dist}
License:          GPLv3+
URL:              http://cangjians.github.io/projects/%{name}
Source0:          https://github.com/Cangjians/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz

BuildArch:        noarch

BuildRequires:    desktop-file-utils
BuildRequires:    gcc
BuildRequires:    ibus-devel
BuildRequires:    intltool
BuildRequires:    python3-devel

# For the unit tests
BuildRequires:    gobject-introspection
BuildRequires:    gtk3
BuildRequires:    python3-cangjie >= 1.2
BuildRequires:    python3-gobject

Requires:         gobject-introspection
Requires:         gtk3
Requires:         python3-canberra
Requires:         python3-cangjie >= 1.2
Requires:         python3-gobject

%description
Common files needed by the IBus engines for users of the Cangjie and Quick
input methods.


%package engine-cangjie
Summary:          Cangjie input method for IBus
Requires:         %{name} = %{version}-%{release}

%description engine-cangjie
IBus engine for users of the Cangjie input method.

It is primarily intended to Hong Kong people who want to input Traditional
Chinese, as they are (by far) the majority of Cangjie users.

However, it should work for others as well (e.g to input Simplified Chinese).


%package engine-quick
Summary:          Quick (Simplified Cangjie) input method for IBus
Requires:         %{name} = %{version}-%{release}

%description engine-quick
IBus engine for users of the Quick (Simplified Cangjie) input method.

It is primarily intended to Hong Kong people who want to input Traditional
Chinese, as they are (by far) the majority of Quick users.

However, it should work for others as well (e.g to input Simplified Chinese).


%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot} INSTALL="install -p"

%find_lang %{name}


%check
make check

# Upstream doesn't validate their desktop files
desktop-file-validate %{buildroot}/%{_datadir}/applications/ibus-setup-cangjie.desktop
desktop-file-validate %{buildroot}/%{_datadir}/applications/ibus-setup-quick.desktop



%files -f %{name}.lang
%doc AUTHORS README.md
%license COPYING
%{_bindir}/ibus-setup-cangjie
%{python3_sitelib}/%{module_name}
%{_datadir}/%{name}
%{_datadir}/glib-2.0/schemas/org.cangjians.ibus.*.gschema.xml
%{_datadir}/icons/hicolor/*/intl/*

# Using %%{_prefix}/lib is allowed here because the package is exempt from
# multilib (because it is noarch), see:
#     https://fedoraproject.org/wiki/Packaging:Guidelines#Multilib_Exempt_Locations
%{_prefix}/lib/%{name}

%files engine-cangjie
%{_datadir}/applications/ibus-setup-cangjie.desktop
%{_datadir}/appdata/cangjie.appdata.xml
%{_datadir}/ibus/component/cangjie.xml

%files engine-quick
%{_datadir}/applications/ibus-setup-quick.desktop
%{_datadir}/appdata/quick.appdata.xml
%{_datadir}/ibus/component/quick.xml


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.4-20
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.4-18
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.4-17
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Mathieu Bridon <bochecha@daitauha.fr> - 2.4-15
- Add missing requirements.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.4-12
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.4-10
- Remove obsolete scriptlets

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.4-7
- Rebuild for Python 3.6

* Thu Aug 18 2016 Mathieu Bridon <bochecha@daitauha.fr> - 2.4-6
- Drop the GSettings schema scriptlets, they are unneeded for Fedora >= 24.

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Mar 29 2015 Mathieu Bridon <bochecha@daitauha.fr> - 2.4-1
- Update to 2.4.

* Wed Mar 04 2015 Mathieu Bridon <bochecha@daitauha.fr> - 2.3-1
- Update to 2.3.

* Thu Jul 10 2014 Mathieu Bridon <bochecha@fedoraproject.org> - 2.2-4
- Split the engines into their own subpackages.
  This makes much more sense for users of a graphical package manager (like
  GNOME Software): installing one installs just that, and more importantly
  removing an engine doesn't remove the other one.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Fri Apr 25 2014 Mathieu Bridon <bochecha@fedoraproject.org> - 2.2-1
- New upstream 2.2 release.

* Sun Feb 02 2014 Mathieu Bridon <bochecha@fedoraproject.org> - 2.1-1
- New upstream 2.1 release.

* Tue Dec 24 2013 Mathieu Bridon <bochecha@fedoraproject.org> - 2.0-1
- New upstream 2.0 release.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 07 2013 Mathieu Bridon <bochecha@fedoraproject.org> - 1.0-3
- Preserve the file timestamps on installation.

* Mon May 06 2013 Mathieu Bridon <bochecha@fedoraproject.org> - 1.0-2
- Comment on the usage of %%{_prefix}/lib
- Validate the desktop file.

* Thu May 02 2013 Mathieu Bridon <bochecha@fedoraproject.org> - 1.0-1
- Initial package for Fedora.
