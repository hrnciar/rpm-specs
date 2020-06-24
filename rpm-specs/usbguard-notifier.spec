Name:           usbguard-notifier
Version:        0.0.6
Release:        1%{?dist}
Summary:        A tool for detecting usbguard policy and device presence changes

License:        GPLv2+
URL:            https://github.com/Cropi/%{name}
Source0:        https://github.com/Cropi/usbguard-notifier/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz

Requires: systemd

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: autoconf automake libtool make
BuildRequires: usbguard-devel
BuildRequires: librsvg2-devel
BuildRequires: libnotify-devel
BuildRequires: asciidoc
BuildRequires: catch1-devel
BuildRequires: execstack
BuildRequires: systemd-rpm-macros

%description
USBGuard Notifier software framework detects usbguard policy modifications
as well as device presence changes and displays them as pop-up notifications.

%prep
%setup -q

%build
mkdir -p ./m4
autoreconf -i -f -v --no-recursive ./

export CXXFLAGS="$RPM_OPT_FLAGS"

%configure \
    --disable-silent-rules \
    --without-bundled-catch \
    --enable-debug-build

%set_build_flags
make %{?_smp_mflags}

%check
make check

%install
make install INSTALL='install -p' DESTDIR=%{buildroot}
execstack -c %{buildroot}%{_bindir}/usbguard-notifier
execstack -c %{buildroot}%{_bindir}/usbguard-notifier-cli

%post
%systemd_user_post %{name}.service

%preun
%systemd_user_preun %{name}.service

%postun
%systemd_user_postun_with_restart %{name}.service

%files
%doc README.md CHANGELOG.md
%license LICENSE
%{_bindir}/usbguard-notifier
%{_bindir}/usbguard-notifier-cli
%{_mandir}/man1/usbguard-notifier.1.gz
%{_mandir}/man1/usbguard-notifier-cli.1.gz
%{_userunitdir}/usbguard-notifier.service


%changelog
* Wed Apr 29 2020 Attila Lakatos <alakatos@redhat.com> 0.0.6-1
- Rebase to 0.0.6

* Fri Feb 21 2020 Attila Lakatos <alakatos@redhat.com> 0.0.5-1
- Initial package
