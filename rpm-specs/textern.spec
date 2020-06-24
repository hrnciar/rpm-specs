%global commit          5339fb6ae33c72c27f2769d0fc3dabb6191b5d3a
%global shortcommit     %(c=%{commit}; echo ${c:0:7})
%global snapshotdate    20180821
%global debug_package   %nil

# this enforces us to create non-noarch package
%global native_dir      %_libdir/mozilla/native-messaging-hosts

%global __brp_python_bytecompile :

Name:           textern
Version:        0
Release:        0.8.%{snapshotdate}git%shortcommit%{?dist}
Summary:        Firefox add-on for editing text in your favorite external editor

License:        GPLv3+
URL:            https://github.com/jlebon/textern

Source0:        %url/archive/%{shortcommit}/%{name}-%{commit}.tar.gz

# Original Makefile's LIBEXEC doesn't respect $(DESTDIR)
# https://github.com/jlebon/textern/pull/36
Patch0:         textern-5339fb6-build.patch

# https://github.com/jlebon/textern/pull/57
Patch1:         compat-for-new-inotify-simple.patch

Requires:       mozilla-filesystem
Requires:       python3-inotify_simple

BuildRequires:  make
BuildRequires:  python3-devel

%description
Textern is a Firefox add-on that allows you to edit text areas in web pages
using an external editor.  It is similar in functionality to the popular
It's All Text! add-on, though makes use of the WebExtension API and is thus
fully compatible with multiprocessing and supported beyond Firefox 57.

This is not a self-standing Firefox add-on, it's only the "native" application
used by Add-on named "textern".  Please install the Add-on manually.


%prep
%autosetup -p1 -n %name-%commit


%build


%install
make native-install \
    PREFIX=/usr \
    MOZILLA_NATIVE=%native_dir \
    DESTDIR=%buildroot


%files
%license LICENSE
%doc README.md
%dir %native_dir
%native_dir/textern.json
%dir %_libexecdir/textern
%_libexecdir/textern/textern.py


%changelog
* Tue Feb 18 2020 Pavel Raiskup <praiskup@redhat.com> - 0-0.8.20180821git5339fb6
- compat with new inotify simple

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.20180821git5339fb6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.20180821git5339fb6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.20180821git5339fb6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Aug 22 2018 Pavel Raiskup <praiskup@redhat.com> - 0-0.4.20180821git5339fb6
- fix spec License to GPLv3+, per rhbz#1619528

* Tue Aug 21 2018 Pavel Raiskup <praiskup@redhat.com> - 0-0.3.20180821git5339fb6
- fix versioning and other problems spotted by Robert-André Mauchin
  and Lukáš Tyrychtr (rhbz#1619528)

* Tue Aug 21 2018 Pavel Raiskup <praiskup@redhat.com> - 0.git5339fb6-3
- actually drop noarch, but don't generate debuginfo

* Tue Aug 21 2018 Pavel Raiskup <praiskup@redhat.com> - 0.git5339fb6-2
- s/simple_inotify/inotify_simple/

* Tue Aug 21 2018 Pavel Raiskup <praiskup@redhat.com> - 0.git5339fb6-1
- initial rpm packaging
