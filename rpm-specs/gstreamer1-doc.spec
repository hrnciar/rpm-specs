%global         majorminor      1.0

Name:           gstreamer1-doc
Version:        1.18.0
Release:        1%{?dist}
BuildArch:      noarch
Summary:        GStreamer documentation

# All tutorial code is licensed under any of the following licenses (your choice):
#  2-clause BSD license ("simplified BSD license") (LICENSE.BSD)
#  MIT license (LICENSE.MIT)
#  LGPL v2.1 (LICENSE.LGPL-2.1)
# Application Developer Manual and Plugin Writer's Guide
#  Open Publication License v1.0 (LICENSE.OPL), for historical reasons.
# Documentation
#  Creative Commons CC-BY-SA-4.0 license, but some parts of the documentation
#  may still be licensed differently (e.g. LGPLv2.1) for historical reasons.
License:        (BSD or MIT or LGPLv2+) and Open Publication and CC-BY-SA
URL:            http://gstreamer.freedesktop.org/
Source0:        https://gstreamer.freedesktop.org/src/gstreamer-docs/gstreamer-docs-%{version}.tar.xz

%description
GStreamer documentation.

%prep
%setup -q -n gstreamer-docs-%{version}

%install

# move devhelp into the right directory
mkdir -p $RPM_BUILD_ROOT%{_datadir}/gtk-doc/html/
mv devhelp/books/GStreamer $RPM_BUILD_ROOT%{_datadir}/gtk-doc/html/GStreamer-%{majorminor}
# Remove the search assets, we use devhelp search
rm -rf $RPM_BUILD_ROOT%{_datadir}/gtk-doc/html/GStreamer-%{majorminor}/assets/js/search
# Rename the devhelp docs to include the version
mv $RPM_BUILD_ROOT%{_datadir}/gtk-doc/html/GStreamer-%{majorminor}/GStreamer.devhelp2 \
   $RPM_BUILD_ROOT%{_datadir}/gtk-doc/html/GStreamer-%{majorminor}/GStreamer-%{majorminor}.devhelp2

%files
%doc README.md html
%{_datadir}/gtk-doc/html/GStreamer-%{majorminor}/

%changelog
* Tue Sep 8 2020 Wim Taymans <wtaymans@redhat.com> - 1.18.0-1
- Update to version 1.18.0

* Fri Aug 21 2020 Wim Taymans <wtaymans@redhat.com> - 1.17.90-1
- Update to version 1.17.90

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 8 2020 Wim Taymans <wtaymans@redhat.com> - 1.17.2-2
- BuildArch: noarch
- Correct License: field and clarify breakdown
- Small cleanups (see rhbz#1854392)

* Tue Jul 7 2020 Wim Taymans <wtaymans@redhat.com> - 1.17.2-1
- Initial version 1.17.2
