%global uuid argos@pew.worldwidemann.com

%global commit fcb475140bd9d0b4b95279ce56c4c28f36fb29d6
%global shortcommit fcb4751
%global snapshot_date 20200110
%global snapinfo %{snapshot_date}.%{shortcommit}

Name:           gnome-shell-extension-argos
Version:        3
Release:        2.%{snapinfo}%{?dist}
Summary:        Create GNOME Shell extensions in seconds

License:        GPLv3
URL:            https://github.com/p-e-w/argos
Source0:        %{url}/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz
# Use registerClass for GNOME 3.36 compatibility
# https://github.com/p-e-w/argos/pull/111
Patch0:         %{url}/pull/111.patch#/argos-registerclass.patch

BuildArch:      noarch

Requires:       gnome-shell >= 3.36.0

%description
Most GNOME Shell extensions do one thing: Add a button with a dropdown menu to
the panel, displaying information and exposing functionality. Even in its
simplest form, creating such an extension is a nontrivial task involving a
poorly documented and ever-changing JavaScript API.

Argos lets you write GNOME Shell extensions in a language that every Linux user
is already intimately familiar with: Bash scripts.

More precisely, Argos is a GNOME Shell extension that turns executables'
standard output into panel dropdown menus. It is inspired by, and fully
compatible with, the BitBar app for macOS. Argos supports many BitBar plugins
without modifications, giving you access to a large library of well-tested
scripts in addition to being able to write your own.


%prep
%autosetup -p1 -n argos-%{commit}


%build


%install
mkdir -p %{buildroot}/%{_datadir}/gnome-shell/extensions/
cp -pr %{uuid} %{buildroot}%{_datadir}/gnome-shell/extensions/


%files
# asked upstream to include license text:
# https://github.com/p-e-w/argos/pull/115
%doc README.md
%{_datadir}/gnome-shell/extensions/%{uuid}/


%changelog
* Tue Apr 28 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 3.2.20200110.fcb4751
- add URLs to pull requests for reference

* Thu Apr 23 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 3-1.20200110.fcb4751
- Initial Fedora package
