# ***********************************************************************
# *                                                                     *
# *            Star Traders: A Game of Interstellar Trading             *
# *               Copyright (C) 1990-2020, John Zaitseff                *
# *                                                                     *
# ***********************************************************************

# Author: John Zaitseff <J.Zaitseff@zap.org.au>
# $Id: fa294d8ca46be524f8fce9fbe172f160eb8d285e $

# This file is distributed under the same licence as Star Traders itself:
# the GNU General Public License, version 3 or later.

Name:           trader
Version:        7.14
Release:        2%{?dist}
Summary:        Star Traders, a simple game of interstellar trading
License:        GPLv3+
Url:            https://www.zap.org.au/projects/trader/
Source0:        https://ftp.zap.org.au/pub/trader/unix/trader-%{version}.tar.xz

BuildRequires:  gcc gettext pkgconfig(ncurses) desktop-file-utils gperf
Provides:       bundled(gnulib)

%description
Star Traders is a simple game of interstellar trading, where the objective
is to create companies, buy and sell shares, borrow and repay money, in
order to become the wealthiest player (the winner).

%global _hardened_build 1

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install
%find_lang %{name}
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files -f %{name}.lang
%doc README NEWS
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man6/%{name}.6*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*

%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 09 2020 John Zaitseff <J.Zaitseff@zap.org.au> - 7.14-1
- Updated the RPM package for a new release of Star Traders: version 7.14.

* Thu Nov 14 2019 John Zaitseff <J.Zaitseff@zap.org.au> - 7.13-2
- Removed obsolete gtk-update-icon-cache scriplets.

* Thu Nov 14 2019 John Zaitseff <J.Zaitseff@zap.org.au> - 7.13-1
- Updated the RPM package for a new release of Star Traders: version 7.13.

* Wed Aug 30 2017 John Zaitseff <J.Zaitseff@zap.org.au> - 7.12-1
- Updated the RPM package for a new release of Star Traders: version 7.12.

* Sun Jun 18 2017 John Zaitseff <J.Zaitseff@zap.org.au> - 7.11-1
- Updated the RPM package for a new release of Star Traders: version 7.11.

* Sun Jun 04 2017 John Zaitseff <J.Zaitseff@zap.org.au> - 7.10-2
- Removed superfluous slash in desktop-file-validate command line.

* Fri Jun 02 2017 John Zaitseff <J.Zaitseff@zap.org.au> - 7.10-1
- Updated the RPM package for a new release of Star Traders: version 7.10.
- Changed a dependency from ncurses-devel to pkgconfig(ncurses), now that
  the Autoconf macro uses pkg-config.
- Added a dependency on gcc, as per the Fedora Packaging Guidelines for C
  programs.
- Added a dependency on desktop-file-utils for the desktop file.
- Install the desktop file and icons now shipped with Star Traders.
- Install the COPYING file to /usr/share/licenses/trader.
- Use generic make_build and make_install macros.

* Tue Jan 05 2016 John Zaitseff <J.Zaitseff@zap.org.au> - 7.9-1
- Updated the RPM package for a new release of Star Traders: version 7.9.

* Thu Sep 10 2015 John Zaitseff <J.Zaitseff@zap.org.au> - 7.8-1
- Updated the RPM package for a new release of Star Traders: version 7.8.

* Tue Aug 18 2015 John Zaitseff <J.Zaitseff@zap.org.au> - 7.7-1
- Updated the RPM package for a new release of Star Traders: version 7.7.

* Wed Aug 13 2014 John Zaitseff <J.Zaitseff@zap.org.au> - 7.6-1
- Updated the RPM package for a new release of Star Traders: version 7.6.

* Sat May 24 2014 John Zaitseff <J.Zaitseff@zap.org.au> - 7.5-1
- Updated the RPM package for a new release of Star Traders: version 7.5.

* Wed Oct 03 2012 John Zaitseff <J.Zaitseff@zap.org.au> - 7.4-3
- Added a dependency on gperf: it may be required for gnulib.

* Thu Sep 20 2012 John Zaitseff <J.Zaitseff@zap.org.au> - 7.4-2
- Simplified the RPM spec file to suit Fedora guidelines.

* Wed May 09 2012 John Zaitseff <J.Zaitseff@zap.org.au> - 7.4-1
- Updated the RPM package for a new release of Star Traders: version 7.4.

* Mon Apr 30 2012 John Zaitseff <J.Zaitseff@zap.org.au> - 7.3.99.2-2
- Changed the RPM spec file to remove OpenSUSE-specific sections

* Mon Apr 16 2012 John Zaitseff <J.Zaitseff@zap.org.au> - 7.3.99.2-1
- Initial RPM package of Star Traders.

