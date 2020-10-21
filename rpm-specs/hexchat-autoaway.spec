# EL8 and earlier does not have _vpath_builddir defined
%{?!_vpath_builddir:%define _vpath_builddir %{_target_platform}}

%if %{?cmake_build:1}%{?!cmake_build:0}
%global old_build 0
%else
%global old_build 1
%endif

%if 0%{?rhel} > 0 || 0%{?rhel} <= 8
# Bug 1883094 - hexchat-autoaway failed to build in aarch64 because hexchat-devel is missing
ExcludeArch:    aarch64
# Bug 1883095 - hexchat-autoaway failed to build in 390x because hexchat-devel is missing
ExcludeArch:    s390x
%endif
Name:           hexchat-autoaway
Version:        2.0
Release:        5%{?dist}
Summary:        HexChat plugin that automatically mark you away

License:        GPLv3+
URL:            https://github.com/andreyv/hexchat-autoaway
Source0:        https://github.com/andreyv/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

## Upstream PR#3 "feat(away-nick-suffix): append away suffix to nickname"
Patch0:         https://patch-diff.githubusercontent.com/raw/andreyv/hexchat-autoaway/pull/3.patch#/0001-append-away-suffix-to-nickname.patch

BuildRequires:  cmake3
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  gtk2-devel >= 2.14
BuildRequires:  hexchat-devel
BuildRequires:  libXScrnSaver-devel
Requires: gtk2 >= 2.14
Requires: hexchat

%description
This HexChat plugin will automatically mark you away when your
computer is idle. It works on systems that use the GTK+ X11
backend, such as GNU/Linux.

%prep
%autosetup -S git_am

%build
%if %old_build
mkdir -p %_vpath_builddir
cd %_vpath_builddir && %cmake3 -DCMAKE_BUILD_TYPE=Release ..
%make_build
cd -
%else
%cmake -DCMAKE_BUILD_TYPE=Release
%cmake_build
%endif

%install
%if %old_build
%make_install -C %_vpath_builddir
%else
%cmake_install
%endif

%files
%license COPYING
%doc README.md
%{_libdir}/hexchat/plugins/libautoaway.so

%changelog
* Tue Sep 29 2020 Ding-Yi Chen <dchen@redhat.com> - 2.0-5
- Fix conditional build

* Mon Sep 28 2020 Ding-Yi Chen <dchen@redhat.com> - 2.0-4
- ExcludeArch s390x and aarch64 because hexchat-devel is missing

* Sun Sep 20 2020 Ding-Yi Chen <dchen@redhat.com> - 2.0-3
- Change the patch filename as suggested in package review.
- Fix for koji build

* Mon Sep 07 2020 Ding Yi Chen <dchen@redhat.com> - 2.0-2
- Remove upstream pull request #2, as it is invalid.
- Add upstream pull request #3
  feat(away-nick-suffix): append away suffix to nickname

* Sun Jul 26 2020 Ding Yi Chen <dchen@redhat.com> - 2.0-1
- Initial packaging
