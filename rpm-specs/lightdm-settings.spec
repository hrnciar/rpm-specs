Name:		lightdm-settings
Version:	1.4.2
Release:	1%{?dist}
Summary:	Configuration tool for the LightDM display manager

License:	GPLv3+
URL:		https://github.com/linuxmint/%{name}
Source0:	%{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:	noarch

BuildRequires:	desktop-file-utils
BuildRequires:	gettext

Requires:	filesystem
Requires:	hicolor-icon-theme
Requires:	polkit
Requires:	python3-xapp
Requires:	python3-gobject
Requires:	python3-setproctitle
Requires:	slick-greeter

%description
This tool currently lets users configure slick-greeter.


%prep
%autosetup -p 1

# Clean she-bangs.
for f in .%{_prefix}/lib/%{name}/*.py ; do
	%{__sed} -e '/^#!.*/d' < ${f} > ${f}.new
	/bin/touch -r ${f} ${f}.new
	%{__mv} -f ${f}.new ${f}
done

# Use pkexec.
f=".%{_bindir}/%{name}"
%{__sed} -e 's!support_pkexec=False!support_pkexec=True!g'		\
	< ${f} > ${f}.new
/bin/touch -r ${f} ${f}.new
%{__mv} -f ${f}.new ${f}


%build
%make_build


%install
# No install-target in Makefile.
%{__cp} -pr .%{_prefix} %{buildroot}

# Set exec-permissions where needed.
%{__chmod} -c 0755 %{buildroot}%{_bindir}/%{name}			\
	 %{buildroot}%{_prefix}/lib/%{name}/%{name}

# Find localizations and build manifest.
%find_lang %{name}


%check
%{_bindir}/desktop-file-validate					\
	%{buildroot}%{_datadir}/applications/*.desktop


%files -f %{name}.lang
%license debian/copyright COPYING
%doc debian/changelog README.md
%{_bindir}/%{name}
%{_prefix}/lib/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/polkit-1/actions/org.x.%{name}.policy


%changelog
* Wed Jun 17 2020 Leigh Scott <leigh123linux@gmail.com> - 1.4.2-1
- Update to 1.4.2 release

* Wed Jun 17 2020 Leigh Scott <leigh123linux@gmail.com> - 1.4.1-1
- Update to 1.4.1 release

* Tue May 12 2020 Leigh Scott <leigh123linux@gmail.com> - 1.4.0-1
- Update to 1.4.0 release

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 09 2020 Leigh Scott <leigh123linux@googlemail.com> - 1.3.3-1
- Update to 1.3.3 release

* Wed Dec 11 2019 Leigh Scott <leigh123linux@googlemail.com> - 1.3.2-1
- Update to 1.3.2 release

* Tue Nov 26 2019 Leigh Scott <leigh123linux@googlemail.com> - 1.3.1-1
- Update to 1.3.1 release

* Fri Nov 22 2019 Leigh Scott <leigh123linux@googlemail.com> - 1.3.0-1
- Update to 1.3.0 release

* Wed Jul 31 2019 Leigh Scott <leigh123linux@googlemail.com> - 1.2.8-1
- Update to 1.2.8 release

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jul 14 2019 Leigh Scott <leigh123linux@googlemail.com> - 1.2.7-1
- Update to 1.2.7 release

* Sun Jun 30 2019 Leigh Scott <leigh123linux@googlemail.com> - 1.2.6-1
- Update to 1.2.6 release

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Dec 16 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.2.5-1
- Update to 1.2.5 release

* Tue Nov 27 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.2.4-1
- Update to 1.2.4 release

* Wed Aug 15 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.2.3-1
- Update to 1.2.3 release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun May 27 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.2.1-1
- Update to 1.2.1 release

* Thu May 10 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.2.0-1
- Update to 1.2.0 release

* Thu Feb 15 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.1.4-1
- Update to 1.1.4 release

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Nov 06 2017 Björn Esser <besser82@fedoraproject.org> - 1.1.3-1
- Update to 1.1.3 release (rhbz#1509947)

* Fri Oct 27 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.1.2-1
- Update to 1.1.2 release

* Thu Aug 31 2017 Björn Esser <besser82@fedoraproject.org> - 1.1.1-6
- Preserve mode of files when changing hashbang

* Thu Aug 31 2017 Björn Esser <besser82@fedoraproject.org> - 1.1.1-5
- Fix hashbangs for EPEL

* Tue Aug 29 2017 Björn Esser <besser82@fedoraproject.org> - 1.1.1-4
- Another fix for EPEL

* Tue Aug 29 2017 Björn Esser <besser82@fedoraproject.org> - 1.1.1-3
- Adjustments for EPEL

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 30 2017 Björn Esser <besser82@fedoraproject.org> - 1.1.1-1
- Update to 1.1.1 release (rhbz#1466545)

* Tue Jun 13 2017 Björn Esser <besser82@fedoraproject.org> - 1.1.0-1
- Update to 1.1.0 release (rhbz#1460470)

* Wed May 31 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.9-1
- Update to 1.0.9 release (rhbz#1455370)

* Thu May 18 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.7-2
- Activate support for pkexec

* Wed May 17 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.7-1
- Update to 1.0.7 release (rhbz#1451532)

* Mon May 15 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.5-1
- Update to 1.0.5 release (rhbz#1450706)

* Sun May 07 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.4-1
- Update to 1.0.4 release (rhbz#1448705)
- Pick up installed locales

* Fri May 05 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.0.3-1
- Update to 1.0.3 release
- Add requires python3-xapp

* Wed Apr 26 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.2-4
- Add missing dependency on python3-setproctitle (rhbz#1444436)

* Sat Apr 08 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.2-3
- Add more patches from upstream

* Fri Apr 07 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.2-2
- Add patches from upstream

* Fri Apr 07 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.2-1
- Initial import (rhbz#1440240)

* Fri Apr 07 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.2-0.1
- Initial rpm-release (rhbz#1440240)
