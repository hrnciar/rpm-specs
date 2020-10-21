%global uuid com.chatterino.chatterino

# Git submodules
# * humanize
%global commit1         4e00a03623966723f23ca3034c1ad944009cd7be
%global shortcommit1    %(c=%{commit1}; echo ${c:0:7})

# * libcommuni
%global commit2         f3e7f97914d9bf1166d349a83d93a2b4f4743c39
%global shortcommit2    %(c=%{commit2}; echo ${c:0:7})

# * settings
%global commit3         a5040463c01e6b0e562eab82e0decb29cab9b450
%global shortcommit3    %(c=%{commit3}; echo ${c:0:7})

# * signals
%global commit4         1c38746b05d9311e73c8c8acdfdc4d36c9c551be
%global shortcommit4    %(c=%{commit4}; echo ${c:0:7})

# * serialize
%global commit5         130ffc3ec722284ca454a1e70c5478a75f380144
%global shortcommit5    %(c=%{commit5}; echo ${c:0:7})

# * rapidjson
%global commit6         d87b698d0fcc10a5f632ecbc80a9cb2a8fa094a5
%global shortcommit6    %(c=%{commit6}; echo ${c:0:7})

# * websocketpp
%global commit7         1e0138c7ccedc6be859d28270ccd6195f235a94e
%global shortcommit7    %(c=%{commit7}; echo ${c:0:7})

# * qtkeychain
%global commit8         832f550da3f6655168a737d2e1b7df37272e936d
%global shortcommit8    %(c=%{commit8}; echo ${c:0:7})

Name:           chatterino2
Version:        2.1.7
Release:        3%{?dist}
Summary:        Chat client for twitch.tv

# Boost Software License (v1.0) Boost Software License 1.0
# -----------------------------------------------------------------------
# resources/licenses/boost_boost.txt
#
# BSD 2-clause "Simplified" License
# ---------------------------------
# lib/fmt/
#
# BSD 3-clause "New" or "Revised" License
# ---------------------------------------
# lib/libcommuni/
# lib/websocketpp/
#
# Expat License
# -------------
# lib/humanize/
# lib/serialize/
# lib/signals/
# lib/websocketpp/
# resources/
#
# Mozilla Public License (v1.1) GNU General Public License (v2 or later) or GNU Lesser General Public License (v2.1 or later)
# ---------------------------------------------------------------------------------------------------------------------------
# lib/libcommuni/
#
# zlib/libpng license Aladdin Free Public License
# -----------------------------------------------
# lib/websocketpp/
#
License:        MIT and Boost and BSD and zlib and GPLv2+ and LGPLv2+ and MPLv1.1

URL:            https://github.com/Chatterino/chatterino2
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/pajlada/humanize/archive/%{commit1}/humanize-%{shortcommit1}.tar.gz
Source2:        https://github.com/hemirt/libcommuni/archive/%{commit2}/libcommuni-%{shortcommit2}.tar.gz
Source3:        https://github.com/pajlada/settings/archive/%{commit3}/settings-%{shortcommit3}.tar.gz
Source4:        https://github.com/pajlada/signals/archive/%{commit4}/signals-%{shortcommit4}.tar.gz
Source5:        https://github.com/pajlada/serialize/archive/%{commit5}/serialize-%{shortcommit5}.tar.gz
Source6:        https://github.com/Tencent/rapidjson/archive/%{commit6}/rapidjson-%{shortcommit6}.tar.gz
Source7:        https://github.com/ziocleto/websocketpp/archive/%{commit7}/websocketpp-%{shortcommit7}.tar.gz
Source8:        https://github.com/Chatterino/qtkeychain/archive/%{commit8}/qtkeychain-%{shortcommit8}.tar.gz

#BuildRequires:  ninja-build
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  libsecret-devel
BuildRequires:  openssl-devel
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Multimedia)
BuildRequires:  cmake(Qt5Svg)

# Modules
# * For future, maybe
#BuildRequires:  fmt-devel
#BuildRequires:  libcommuni-devel
BuildRequires:  rapidjson-devel
#BuildRequires:  websocketpp-devel

Requires:       hicolor-icon-theme

# All submodules patched so not possible to build with system packages
#
# * Do note that fmt needs to be version 4 for it to work with Chatterino
# - https://github.com/Chatterino/chatterino2/issues/1444#issuecomment-567679616
Provides:       bundled(fmt) = 4

Provides:       bundled(humanize) = 0~git%{shortcommit1}
Provides:       bundled(libcommuni) = 3.5.0
Provides:       bundled(qtkeychain) = 0.9.1~git%{shortcommit8}
Provides:       bundled(serialize) = 0~git%{shortcommit5}
Provides:       bundled(settings) = 0~git%{shortcommit3}
Provides:       bundled(signals) = 0~git%{shortcommit4}
Provides:       bundled(websocketpp) = 0.8.1

%description
Chatterino 2 is the second installment of the Twitch chat client series
"Chatterino".


%prep
%setup -q
%setup -q -D -T -a1
%setup -q -D -T -a2
%setup -q -D -T -a3
%setup -q -D -T -a4
%setup -q -D -T -a5
%setup -q -D -T -a6
%setup -q -D -T -a7
%setup -q -D -T -a8

mv humanize-%{commit1}/*    lib/humanize
mv libcommuni-%{commit2}/*  lib/libcommuni
mv settings-%{commit3}/*    lib/settings
mv signals-%{commit4}/*     lib/signals
mv serialize-%{commit5}/*   lib/serialize
mv rapidjson-%{commit6}/*   lib/rapidjson
mv websocketpp-%{commit7}/* lib/websocketpp
mv qtkeychain-%{commit8}/*  lib/qtkeychain

# Unbundling
# * https://github.com/Chatterino/chatterino2/issues/1444
pushd lib/
rm -r   rapidjson/  \
        qBreakpad/  \
        WinToast/
popd

mkdir -p %{_target_platform}


%build
pushd %{_target_platform}
%qmake_qt5                          \
    PREFIX=%{buildroot}%{_prefix}   \
    RAPIDJSON_SYSTEM=1              \
    ..
popd

%make_build -C %{_target_platform}


%install
%make_install -C %{_target_platform}
install -m 0644 -Dp resources/%{uuid}.appdata.xml   \
    %{buildroot}%{_metainfodir}/%{uuid}.appdata.xml
install -m 0644 -Dp resources/icon.png              \
    %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/chatterino.png


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files
%license LICENSE
%doc README.md BUILDING_ON_LINUX.md docs/
%{_bindir}/chatterino
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/*/*.png
%{_metainfodir}/*.xml


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 30 2020 Jonathan Wakely <jwakely@redhat.com> - 2.1.7-2
- Rebuilt for Boost 1.73

* Fri Feb 28 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.1.7-1
- Update to 2.1.7
- Add new submodule 'qtkeychain'
- Drop patches (upstreamed now)
- Disable LTO

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 21 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 2.1.4-8
- Build with system 'rapidjson'

* Fri Dec 13 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 2.1.4-7
- Initial package
