Name:		synapse
Version:	0.2.99.4
Release:	6%{?dist}
Summary:	A semantic launcher written in Vala

License:	GPLv3+
URL:		https://launchpad.net/synapse-project
Source0:	https://launchpad.net/synapse-project/0.3/%{version}/+download/%{name}-%{version}.tar.xz

BuildRequires: desktop-file-utils
BuildRequires: gcc
BuildRequires: gettext
BuildRequires: gtk3-devel
BuildRequires: intltool
BuildRequires: json-glib-devel
BuildRequires: libgee-devel
BuildRequires: keybinder3-devel
BuildRequires: libnotify-devel
BuildRequires: vala-devel
BuildRequires: %{_bindir}/valac
BuildRequires: zeitgeist-devel

%description
Synapse is a semantic launcher written in Vala that you can use to start
applications as well as find and access relevant documents and files by making
use of the Zeitgeist engine.

%prep
%setup -q

%build
%configure --disable-static --enable-zeitgeist=yes --disable-silent-rules
%make_build


%install
%make_install

%find_lang %{name}

desktop-file-install \
--delete-original \
--dir=%{buildroot}%{_datadir}/applications \
%{buildroot}%{_datadir}/applications/synapse.desktop

desktop-file-validate %{buildroot}/%{_datadir}/applications/synapse.desktop

%files -f %{name}.lang
%{!?_licensedir:%global license %%doc}
%license COPYING
%license COPYING.GPL2
%license COPYING.LGPL2.1
%doc README AUTHORS
%{_bindir}/%{name}
%{_datadir}/applications/synapse.desktop
%{_mandir}/man1/synapse.1.*
%{_datadir}/icons/hicolor/scalable/apps/synapse.svg

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.99.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.99.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.99.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb  4 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.2.99.4-3
- BR: gcc, valac

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.99.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.99.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr  9 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.2.99.4-1
- 0.2.99.4
- Fix FTBFS (bug 1556240)

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.99.2-6
- Escape macros in %%changelog

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.99.2-5
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.99.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.99.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.99.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Mar 24 2016 Tonet Jallo <tonet666p@fedoraproject.org> 0.2.99.2-1
- Updated source to 0.2.99.2

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.99.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Sep 08 2015 Tonet Jallo <tonet666p@fedoraproject.org> - 0.2.99.1-6
- Corrected labels in changelog
- Added --disable-silent-rules to configure label
- Two license files added

* Thu Aug 27 2015 Tonet Jallo <tonet666p@fedoraproject.org> - 0.2.99.1-5
- The defattr label was removed
- make %%{?_smp_mflags} was replaced instead make_build label
- Source URL was modified a bit at version

* Tue Aug 25 2015 Tonet Jallo <tonet666p@fedoraproject.org> - 0.2.99.1-4
- gtk2-devel was removed from BuildRequires
- glib2-devel was removed from BuildRequires

* Sun Aug 23 2015 Tonet Jallo <tonet666p@fedoraproject.org> - 0.2.99.1-3
- Removing some spaces from SPEC file.

* Sun Aug 23 2015 Tonet Jallo <tonet666p@fedoraproject.org> - 0.2.99.1-2
- Removing some spaces and comments from SPEC file.

* Sun Aug 23 2015 Tonet Jallo <tonet666p@fedoraproject.org> - 0.2.99.1-1
- Initial packaging of retired package.
