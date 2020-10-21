Name:           signon-ui
Version:        0.15
Release:        14%{?dist}
Summary:        Online Accounts Sign-on Ui

License:        GPLv3
URL:            https://launchpad.net/signon-ui

Source0:        https://launchpad.net/signon-ui/trunk/%{version}/+download/signon-ui-%{version}.tar.bz2

Patch0:         signon-ui-0.15-fix-qt5-build.patch

BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtwebkit-devel
BuildRequires:  libaccounts-qt5-devel
BuildRequires:  signon-devel
BuildRequires:  libproxy-devel
BuildRequires:  libnotify-devel

Requires:       dbus

%description
Sign-on UI is the component responsible for handling the user interactions which
can happen during the login process of an online account.
It can show password dialogs and dialogs with embedded web pages.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n signon-ui-%{version}

%patch0 -p1 -b .qt5


%build
export PATH=%{_qt5_bindir}:$PATH
%{qmake_qt5} QMF_INSTALL_ROOT=%{_prefix} \
    CONFIG+=release signon-ui.pro

make %{?_smp_mflags}


%install
make install INSTALL_ROOT=%{buildroot}

# Remove installed tests
rm %{buildroot}/%{_bindir}/signon-ui-unittest
rm %{buildroot}/%{_bindir}/tst_inactivity_timer

# Own directory where others can install provider-specific configuration
mkdir -p %{buildroot}/%{_sysconfdir}/signon-ui/webkit-options.d

%files
%doc README TODO NOTES
%license COPYING
%{_bindir}/signon-ui
%{_datadir}/dbus-1/services/*.service
%{_sysconfdir}/signon-ui

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.15-3
- Rebuilt for GCC 5 C++11 ABI change

* Wed Mar 25 2015 Daniel Vrátil <dvratil@redhat.com> - 0.15-2
- fix license
- fix typo in mkdir arguments
- use %%license

* Tue Mar 17 2015 Daniel Vrátil <dvratil@redhat.com> - 0.15-1
- Initial version
