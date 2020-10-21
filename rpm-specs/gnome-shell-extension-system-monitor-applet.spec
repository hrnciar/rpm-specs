%global extuuid    system-monitor@paradoxxx.zero.gmail.com
%global extdir     %{_datadir}/gnome-shell/extensions/%{extuuid}
%global gschemadir %{_datadir}/glib-2.0/schemas
%global gitname    gnome-shell-system-monitor-applet
%global giturl     https://github.com/paradoxxxzero/%{gitname}

%{!?git_post_release_enabled: %global git_post_release_enabled 1}

%if 0%{?git_post_release_enabled}
  # Git commit is needed for post-release version.
  %global gitcommit 7f8f0a7b255473941f14d1dcaa35ebf39d3bccd0
  %global gitshortcommit %(c=%{gitcommit}; echo ${c:0:7})
  %global gitsnapinfo .20200503git%{gitshortcommit}
%endif

Name:           gnome-shell-extension-system-monitor-applet
Epoch:          1
Version:        38
Release:        9%{?gitsnapinfo}%{?dist}
Summary:        A Gnome shell system monitor extension

# The entire source code is GPLv3+ except convenience.js, which is BSD
License:        GPLv3+ and BSD
URL:            https://extensions.gnome.org/extension/120/system-monitor/
Source0:        %{giturl}/archive/%{?gitcommit}%{!?gitcommit:v%{version}}/%{name}-%{version}%{?gitshortcommit:-%{gitshortcommit}}.tar.gz

BuildArch:      noarch

BuildRequires:  gettext
BuildRequires:  %{_bindir}/glib-compile-schemas

Requires:       gnome-shell-extension-common

# CentOS 7 build environment doesn't support Suggests tag.
%if 0%{?fedora} || 0%{?rhel} >= 8
Suggests:       gnome-tweaks
%endif


%description
Display system information in gnome shell status bar, such as memory usage,
CPU usage, and network rate...


%prep
%autosetup -n %{gitname}-%{?gitcommit}%{!?gitcommit:%{version}} -p 1


%build
%make_build DESTDIR=%{buildroot} BUILD_FOR_RPM=1


%install
%make_install VERSION=%{version} BUILD_FOR_RPM=1

# Cleanup unused files.
%{__rm} -fr %{buildroot}%{extdir}/{COPYING*,README*,locale,schemas}

# Install schema.
%{__mkdir} -p %{buildroot}%{gschemadir}
%{__cp} -pr %{extuuid}/schemas/*gschema.xml %{buildroot}%{gschemadir}

# Install i18n.
%{_bindir}/find %{extuuid} -name '*.po' -print -delete
%{__cp} -pr %{extuuid}/locale %{buildroot}%{_datadir}

# Create manifest for i18n.
%find_lang %{name} --all-name


# CentOS 7 doesn't compile gschemas automatically, Fedora does.
%if 0%{?rhel} && 0%{?rhel} <= 7
%postun
if [ $1 -eq 0 ] ; then
  %{_bindir}/glib-compile-schemas %{gschemadir} &> /dev/null || :
fi

%posttrans
%{_bindir}/glib-compile-schemas %{gschemadir} &> /dev/null || :
%endif


%files -f %{name}.lang
%doc README.md
%license COPYING
%{extdir}
%{gschemadir}/*gschema.xml


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:38-9.20200503git7f8f0a7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 03 2020 Nicolas Viéville <nicolas.vieville@uphf.fr> - 1:38-8.20200503git7f8f0a7
- Updated to last upstream commits
- Fix string warning: Use ByteArray
- Fixed malformed nl translation. Updated makefile to put builds in ./dist
- Cleaned and switched Recommends tag for gnome-tweaks to Suggests tag as dnf
  treats it as Requires tag - RHBZ#1830474

* Thu Apr 16 2020 Nicolas Viéville <nicolas.vieville@uphf.fr> - 1:38-7.20200416git32cc79e
- Updated to last upstream commits
- Support for gnome-shell 3.36 added, and keep legacy usage
- Be able to show preferences from menu
- Make compact work even on resize
- Use UPower directly to remove warning
- Dropped patches (applied upstream)

* Wed Mar 25 2020 Nicolas Viéville <nicolas.vieville@uphf.fr> - 1:38-6.20200325gitcd2704c
- Updated to last upstream commits
- Translate to Turkish language
- Add patch to fix typo nvidia-settings in gpu_usage.sh - RHBZ#1794158
- Add patch to improve fetching values for NVidia GPU usage

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:38-5.20191019gitf00e248
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Oct 19 2019 Nicolas Viéville <nicolas.vieville@uphf.fr> - 1:38-4.20191019gitf00e248
- Updated to last upstream commits
- Use Gio.Subprocess for cleaner child process handling
- Updated Italian Translation
- Updated Slovak translation
- Edited gpu_usage.sh to work with glxinfo
- Included GS 3.34. Fixed formatting
- Removed duplicate css class
- Added Dutch (Netherlands) translation
- Use enums (instead of magic numbers) with GLib.file_test()

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:38-3.20190515gitfc83a73
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 15 2019 Nicolas Viéville <nicolas.vieville@uphf.fr> - 1:38-2.20190515gitfc83a73
- Updated to last upstream commits
- Fix #504  (array.to string() warnings)
- Remove obsolete compatibility code
- Scale width of elements if compact display is on
- Updated translation files
- Reverted ByteArray usage breaking display of thermal and fan speed
- Fixed frequency display showing blank due to ByteArray.tostring

* Mon Apr 29 2019 Nicolas Viéville <nicolas.vieville@uphf.fr> - 1:38-1
- New upstream release (Fedora patches applied - RHBZ#1703693)
- Dropped previous Fedora patches

* Sat Apr 27 2019 Nicolas Viéville <nicolas.vieville@uphf.fr> - 1:36-5.20190427gitc08bfd7
- Updated to last upstream commits
- Reworked Makefile
- Support for gnome-shell 3.32 added
- Added patches to support Fedora RPM package build

* Sun Feb 24 2019 Nicolas Viéville <nicolas.vieville@uphf.fr> - 1:36-4.20190224git2583911
- Updated to last upstream commits
- Get rid of synchronous IO (read)
- Add Japanese translation
- Fix translation for 'GiB' in German
- Add a Makefile target to reload the extension

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:36-3.20190116gitd341bf6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 18 2019 Nicolas Viéville <nicolas.vieville@uphf.fr> - 1:36-2.20190116gitd341bf6
- Updated to last upstream commits
- Updating battery, check prefs
- Bugfix/fix net mount related login hangs after suspend
- Make the log messages more easy to filter from journalctl

* Wed Sep 19 2018 Nicolas Viéville <nicolas.vieville@univ-valenciennes.fr> - 1:36-1.20180919git21ae32a
- Updated to last upstream commits
- Support for gnome-shell 3.30 added
- Close unwanted _stdin_ and _stderr_ file descriptors

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:35-3.20180629gitd0b3a3a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Nicolas Viéville <nicolas.vieville@univ-valenciennes.fr> - 1:35-2.20180629gitd0b3a3a
- Updated to last upstream commits
- Improve post-release versions management

* Tue Apr 10 2018 Nicolas Viéville <nicolas.vieville@univ-valenciennes.fr> - 1:35-1.20180410git751d557
- Updated to last upstream commits
- Added the ability to manage post-release versions (git commit hash) and
  try not to mess up the version schema
- Added VERSION variable to install section to avoid git fatal message

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:33-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Dec 02 2017 Björn Esser <besser82@fedoraproject.org> - 1:33-1
- New upstream release
- Follow upstream versioning
- Bump Epoch since previous people messed up the versioning scheme
- Simplify packaging

* Tue Oct 24 2017 Nicolas Viéville <nicolas.vieville@univ-valenciennes.fr> - 0-0.3.20171005git61b0a60
- Add support for EPEL 7.
- Revert upstream requires - Works with fresh vanilla Fedora with gnome-shell.

* Tue Oct 24 2017 Nicolas Viéville <nicolas.vieville@univ-valenciennes.fr> - 0-0.2.20171005git61b0a60
- Requires libgtop2 and NetworkManager-glib
- Fix NVidia GPU support
- Spec file rework

* Sat Oct 07 2017 Nicolas Viéville <nicolas.vieville@univ-valenciennes.fr> - 0-0.1.20171005git61b0a60
- Spec file cleanup

* Thu Oct 05 2017 Nicolas Viéville <nicolas.vieville@univ-valenciennes.fr> - 0.0.1-0.1.20171005git61b0a60
- Updated to new upstream release
- Fixed battery module error and crash

* Sat Sep 30 2017 Nicolas Viéville <nicolas.vieville@univ-valenciennes.fr> - 0.0.1-0.1.20170930gitf24f167
- Updated to new upstream release
- Added support for Gnome 3.26
- Added GPU usage (NVidia)
- Updated translations

* Thu Sep 28 2017 Nicolas Viéville <nicolas.vieville@univ-valenciennes.fr> - 0.0.1-0.1.20170928git0a9f7a0
- Updated to new upstream release

* Thu Aug 17 2017 Nicolas Viéville <nicolas.vieville@univ-valenciennes.fr> - 0.0.1-0.1.20170817git746f33d
- Updated to new upstream release

* Mon May 01 2017 Nicolas Viéville <nicolas.vieville@univ-valenciennes.fr> - 0.0.1-0.1.20170501git59f443e
- Updated to new upstream release

* Tue Apr 11 2017 Nicolas Viéville <nicolas.vieville@univ-valenciennes.fr> - 0.0.1-0.1.20170411git0948ded
- Updated to new upstream release

* Thu Dec 22 2016 Nicolas Viéville <nicolas.vieville@univ-valenciennes.fr> - 0.0.1-0.1.20161222git3967cdd
- Updated to new upstream release

* Tue Apr 05 2016 Nicolas Viéville <nicolas.vieville@univ-valenciennes.fr> - 0.0.1-0.1.20160405git8b31f07
- Updated to new upstream release

* Wed Sep 30 2015 Nicolas Viéville <nicolas.vieville@univ-valenciennes.fr> - 0.0.1-0.1.20150930git81d1c08
- spec file cleanup
- Updated to new upstream release

* Wed Apr 15 2015 Nicolas Viéville <nicolas.vieville@univ-valenciennes.fr> - 0.0.1-0.1.20150415git44abf9a
- Updated to new upstream release

* Wed Feb 04 2015 Nicolas Viéville <nicolas.vieville@univ-valenciennes.fr> - 0.0.1-0.1.20150204gitd04c136
- Updated to new upstream release
- Added correct %%license tag to license files

* Wed Jan 28 2015 Nicolas Viéville <nicolas.vieville@univ-valenciennes.fr> - 0.0.1-0.1.20150129git6b9973e
- Updated to new upstream release

* Wed Jan 28 2015 Nicolas Viéville <nicolas.vieville@univ-valenciennes.fr> - 0.0.1-0.1.20150128gitccafeef
- Updated to new upstream release

* Fri Oct 10 2014 Nicolas Viéville <nicolas.vieville@univ-valenciennes.fr> - 0.0.1-0.1.git59767af
- Updated to new upstream release

* Wed May 07 2014 Nicolas Viéville <nicolas.vieville@univ-valenciennes.fr> - 0.0.1-0.1.git1b632f9
- Updated to new upstream release

* Wed Mar 06 2013 Nicolas Viéville <nicolas.vieville@univ-valenciennes.fr> - v24-0.1.gitfcecbaa
- Updated to new upstream release

* Sun Jan 13 2013 Nicolas Viéville <nicolas.vieville@univ-valenciennes.fr> - v24-0.1.git3f2c93e
- Updated to new upstream release

* Sun Oct 21 2012 Nicolas Viéville <nicolas.vieville@univ-valenciennes.fr> - v24-0.1.gitec4b4b7
- Updated to new upstream release v24

* Fri Aug 31 2012 Nicolas Viéville <nicolas.vieville@univ-valenciennes.fr> - v18-0.1.git96a05d5
- Updated to new upstream release v18

* Sun Aug 19 2012 Nicolas Viéville <nicolas.vieville@univ-valenciennes.fr> - 2.0b1-0.1.git74500bd
- Updated to new upstream release 2.0b1
- Completed spec file to install translations

* Sun Jun 26 2011 Fabian Affolter <fabian@bernewireless.net> - 1.92-1
- Updated to new upstream release 1.92

* Sat Jun 18 2011 Fabian Affolter <fabian@bernewireless.net> - 1.90-1
- Updated to new upstream release 1.90

* Wed Jun 08 2011 Fabian Affolter <fabian@bernewireless.net> - 0.99-1
- Updated to new upstream release 0.99

* Sat Jun 04 2011 Fabian Affolter <fabian@bernewireless.net> - 0.9-2
- Scriplet updated
- Version condition removed

* Thu Jun 02 2011 Fabian Affolter <fabian@bernewireless.net> - 0.9-1
- Initial package for Fedora
