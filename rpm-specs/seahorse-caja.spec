Summary:        PGP encryption and signing for caja
Name:           seahorse-caja
License:        GPLv2+
Version:        1.18.1
Release:        7%{?dist}
URL:            https://github.com/darkshram/%{name}
Source0:        https://github.com/darkshram/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  mate-common
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(gcr-3)
BuildRequires:  gnupg2
BuildRequires:  gpgme-devel >= 1.0
BuildRequires:  pkgconfig(libcaja-extension)
BuildRequires:  pkgconfig(gnome-keyring-1)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(cryptui-0.0)
BuildRequires:  pkgconfig(libnotify)

%if 0%{?rhel}
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils
%endif

%description
Seahorse caja is an extension for caja which allows encryption
and decryption of OpenPGP files using GnuPG.


%prep
%setup -q

%build
%configure \
    --disable-silent-rules \
    --disable-gpg-check

make %{?_smp_mflags} V=1


%install
%{make_install}

find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'
find %{buildroot} -type f -name "*.a" -exec rm -f {} ';'

desktop-file-validate %{buildroot}%{_datadir}/applications/mate-seahorse-pgp-encrypted.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/mate-seahorse-pgp-keys.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/mate-seahorse-pgp-signature.desktop

%find_lang %{name} --with-gnome --all-name


%if 0%{?rhel} && 0%{?rhel} <= 7
%post
/usr/bin/update-desktop-database &> /dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
    /usr/bin/update-desktop-database &> /dev/null || :
fi

%posttrans
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
%endif

%files -f %{name}.lang
%license COPYING
%doc AUTHORS NEWS
%{_bindir}/mate-seahorse-tool
%{_libdir}/caja/extensions-2.0/libcaja-seahorse.so
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/org.mate.seahorse.caja.*gschema.xml
%{_datadir}/seahorse-caja/
%{_mandir}/man1/mate-seahorse-tool.1*


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Oct 14 2017 Wolfgang Ulbrich <fedora@raveit.de> - 1.18.1-2
- update rpm scriplets

* Sat Oct 14 2017 Wolfgang Ulbrich <fedora@raveit.de> - 1.18.1-1
- initial package
