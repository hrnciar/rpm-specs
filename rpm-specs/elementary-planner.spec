%global appname planner
%global uuid    com.github.alainm23.%{appname}

Name:           elementary-%{appname}
Version:        2.5.4
Release:        1%{?dist}
Summary:        Task manager with Todoist support designed for GNU/Linux

License:        GPLv3+
URL:            https://github.com/alainm23/planner
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala >= 0.40.3
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(granite) >= 0.5
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libecal-2.0)

Requires:       hicolor-icon-theme

%description
How Planner works:

1. Collect your Ideas - The Inbox is your default task list in Planner. When you
add a task, it goes straight to your Inbox unless you specify that the task goes
into a project.

2. Get Organized - Create a project for each of your goals, then add the steps
to reach them. Review these regularly to stay on top of things.

3. Calendar and Events - See your calendar events and plan your time
effectively. Planner will remind you on the right day.

4. Be even more organized - Add a duedate to your tasks, create labels, use
checklists.

Support for Todoist:

- Synchronize your Projects, Task and Sections thanks to Todoist.
- Support for Todoist offline: Work without an internet connection and when
  everything is reconnected it will be synchronized.

* Planner not created by, affiliated with, or supported by Doist

Other features:

- Reminders notifications
- Quick Find
- Night mode


%prep
%autosetup -n %{appname}-%{version} -p1


%build
%meson
%meson_build


%install
%meson_install
%find_lang %{uuid}

# Remove trashy SVG icon dupes
rm -r   %{buildroot}%{_datadir}/icons/hicolor/*@2/      \
        %{buildroot}%{_datadir}/icons/hicolor/48x48/    \
        %{buildroot}%{_datadir}/icons/hicolor/64x64/    


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files -f %{uuid}.lang
%license LICENSE
%doc README.md AUTHORS
%{_bindir}/%{uuid}
%{_bindir}/%{uuid}.quick-add
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/icons/hicolor/*/*/*.svg
%{_metainfodir}/*.xml


%changelog
* Mon Oct 12 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.5.4-1
- build(update): 2.5.4

* Wed Oct  7 21:03:44 EEST 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.5.3-1
- build(update): 2.5.3

* Wed Oct  7 19:58:57 EEST 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.5.2-1
- build(update): 2.5.2

* Sat Oct  3 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.5.1-1
- Update to 2.5.1

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 13 2020 Kevin Fenzi <kevin@scrye.com> - 2.4.6-2
- Rebuild for new evolution-data-server

* Wed Jul 08 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.4.6-1
- Update 2.4.6

* Mon Jun 29 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.4.5-1
- Update 2.4.5

* Sun Jun 28 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.4.4-1
- Update 2.4.4

* Sun Jun 28 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.4.3-1
- Update 2.4.3

* Mon Jun 22 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.4.2-1
- Update 2.4.2

* Thu Apr 30 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.3.5-1
- Update 2.3.5

* Thu Apr 30 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.3.4-1
- Update 2.3.4

* Tue Apr 21 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.3.3-1
- Update 2.3.3

* Sun Apr 19 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.3.2-1
- Update 2.3.2

* Wed Apr 15 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.3.1-1
- Update 2.3.1

* Tue Apr 14 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.2.14-2
- Remove LTO

* Mon Mar 30 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.2.14-1
- Update to 2.2.14

* Fri Feb 21 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.1.1-2
- Initial package
