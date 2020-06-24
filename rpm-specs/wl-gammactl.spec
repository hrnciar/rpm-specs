# -*-Mode: rpm-spec -*-

%global commit       611846ce8f5f6e7fe1afb100416cceb8af54afb2
%global shortcommit  %(c=%{commit}; echo ${c:0:7})

%global proto_name   wlr-protocols
%global proto_url    https://github.com/swaywm/%{proto_name}
%global proto_commit c11408942e2fb54d41dadb84cdf844331076ae11

Name:     wl-gammactl
Version:  0.1
Release:  0.4.20200406git%{shortcommit}%{?dist}
Summary:  Set contrast, brightness and gamma for wayland compositors
License:  MIT
URL:      https://github.com/mischw/wl-gammactl
Source:   %{url}/archive/%{commit}/%{name}-%{commit}.tar.gz
Source1:  %{proto_url}/archive/%{proto_commit}/%{proto_name}-%{proto_commit}.tar.gz

# don't use git to automatically pull wlr-protocols:
Patch0:   wl-gammactl-remove-git.patch
Patch1:   wl-gammactl-add-desktop.patch

BuildRequires: desktop-file-utils
BuildRequires: gcc
BuildRequires: meson
BuildRequires: pkgconfig(gtk+-wayland-3.0)
BuildRequires: pkgconfig(wlroots)

Requires: (sway >= 1.4 if sway)

%description

Small GTK GUI application to set contrast, brightness and gamma for
wayland compositors which support the wlr-gamma-control protocol
extension. Basically this is the example from here:
https://github.com/swaywm/wlroots/blob/master/examples/gamma-control.c
with a nice little GTK GUI slapped on to it. You can set contrast,
brightness and gamma using sliders and reset back to default values.

This was made to make the process of calibrating your monitor a bit
easier, since wayland support for color profiles is not yet
implemented. When you are satisfied with your settings, copy the given
command line and execute it at startup to make the settings load at
apply on every boot.

Keep in mind that it uses the same protocol extension as the
redshift fork
https://aur.archlinux.org/packages/redshift-wlr-gamma-control/

wl-gammactl will kick out any running redshift instance and fail to
start up. On second run it should work as expected. So unfortunately
only one can run at a time (?) for now.

%prep
%autosetup -n %{name}-%{commit}
gzip -dc %{S:1} | tar xf -
mv %{proto_name}-%{proto_commit}/* %{proto_name}/

%build
%meson
%meson_build

%install
%meson_install
desktop-file-install --dir %{buildroot}/%{_datadir}/applications \
    %{name}.desktop

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop

%doc README.md

%license LICENSE

%changelog
* Mon May 04 2020 Bob Hepple <bob.hepple@gmail.com> - 0.1-0.4.20200406git611846c
- rebuilt

* Mon May 04 2020 Bob Hepple <bob.hepple@gmail.com> - 0.1-0.3.20200406git.611846c
- rebuilt per RHBZ#1821172

* Wed Apr 15 2020 Bob Hepple <bob.hepple@gmail.com> - 0.1-0.2.20200406git.611846c
- rebuilt

* Mon Apr 06 2020 Bob Hepple <bob.hepple@gmail.com> - 0.1-0.1.20200406git.611846c
- prep for fedora review

* Wed Feb 19 2020 Bob Hepple <bob.hepple@gmail.com> - 0.1-0.1.20200220git.611846c
- Initial version of the package
