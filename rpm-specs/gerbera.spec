Name:           gerbera
Version:        1.4.0
Release:        3%{?dist}
Summary:        UPnP Media Server
License:        GPLv2 and MIT and OFL
Url:            https://gerbera.io
Source0:        https://github.com/gerbera/gerbera/archive/v%{version}.tar.gz
Source1:        config.xml

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libupnp-devel
BuildRequires:  libuuid-devel
BuildRequires:  expat-devel
BuildRequires:  sqlite-devel
BuildRequires:  duktape-devel
BuildRequires:  curl-devel
BuildRequires:  taglib-devel
BuildRequires:  file-devel
BuildRequires:  libexif-devel
BuildRequires:  exiv2-devel
BuildRequires:  cmake
BuildRequires:  zlib-devel
BuildRequires:  libebml-devel
BuildRequires:  libmatroska-devel
Requires(pre): shadow-utils
%{?systemd_requires}
BuildRequires:  systemd
Requires:       %{name}-data = %{version}-%{release}
 
%description
Gerbera is a UPnP media server which allows you to stream your digital
media through your home network and consume it on a variety of UPnP
compatible devices.

%package data
Summary:        Data files for Gerbera
BuildArch:      noarch

%description data
Data files for the Gerbera media server.

%prep
%autosetup -n %{name}-%{version}

%build
%cmake \
    -DWITH_JS=1 \
    -DWITH_MYSQL=0 \
    -DWITH_CURL=1 \
    -DWITH_TAGLIB=1 \
    -DWITH_MAGIC=1 \
    -DWITH_AVCODEC=0 \
    -DWITH_EXIF=1 \
    -DWITH_EXIV2=1 \
    -DWITH_FFMPEGTHUMBNAILER=0 \
    -DWITH_INOTIFY=1 \
    -DWITH_SYSTEMD=1 \
    -DUPNP_HAS_REUSEADDR=1 .

%make_build

%install
install -p -D -m0644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/gerbera/config.xml
%make_install

# make all files under %%_sysconfdir/gerbera owned by
# this package
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/gerbera
touch $RPM_BUILD_ROOT%{_sysconfdir}/gerbera/{gerbera.db,gerbera.html}
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/log/gerbera
touch $RPM_BUILD_ROOT%{_localstatedir}/log/%{name}
mkdir -p  $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d
cat > $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/%{name} << 'EOF'
/var/log/gerbera/gerbera {
create 644 gerbera gerbera
      monthly
      compress
      missingok
}
EOF


%pre
getent group gerbera >/dev/null || groupadd -r gerbera
getent passwd gerbera >/dev/null || \
useradd -r -g gerbera -d %{_sysconfdir}/gerbera -s /sbin/nologin \
    -c "To run Gerbera" gerbera
exit 0

%post
%systemd_post gerbera.service

%preun
%systemd_preun gerbera.service

%postun
%systemd_postun_with_restart gerbera.service

%files
%license LICENSE.md
%doc AUTHORS CONTRIBUTING.md ChangeLog.md
%attr(-,gerbera,gerbera)%dir %{_sysconfdir}/%{name}/
%attr(-,gerbera,gerbera)%config(noreplace) %{_sysconfdir}/%{name}/*
%attr(-,gerbera,gerbera) %{_localstatedir}/log/%{name}
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%{_sysconfdir}/logrotate.d/
%{_bindir}/%{name}
%{_mandir}/man1/*
%{_unitdir}/gerbera.service

%files data
%{_datadir}/%{name}/
%config(noreplace) %{_datadir}/%{name}/js/import.js
%config(noreplace) %{_datadir}/%{name}/js/playlists.js
%config(noreplace) %{_datadir}/%{name}/js/common.js

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 30 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.4.0-2
- Bump EVR for koji error.

* Mon Dec 30 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.4.0-1
- 1.4.0

* Fri Nov 22 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.3.5-1
- 1.3.5

* Mon Nov 18 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.3.4-1
- 1.3.4

* Wed Oct 30 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.3.3-1
- 1.3.3

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 11 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.3.2-1
- 1.3.2

* Thu Apr 04 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.3.1-1
- 1.3.1

* Thu Feb 21 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.3.0-4
- Drop lastlibfm, liblastfm not working yet.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 30 2019 Rex Dieter <rdieter@fedoraproject.org> - 1.3.0-2
- rebuild (exiv2)

* Tue Jan 29 2019 Gwyn Ciesla <limburgher@gmail.com> - 1.3.0-1
- 1.3.0

* Mon Dec 03 2018 Gwyn Ciesla <limburgher@gmail.com> - 1.2.0-4
- Fix logrotate config, BZ 1655279.

* Mon Nov 12 2018 Gwyn Ciesla <limburgher@gmail.com> - 1.2.0-3
- noconfig js, BZ 1648650.

* Tue Oct 23 2018 Gwyn Ciesla <limburgher@gmail.com> - 1.2.0-2
- Correct log directory.
- Fix default config.

* Fri Oct 05 2018 Dennis Gilmore <dennis@ausil.us> - 1.2.0-1
- update to the 1.2.0 release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-6.20180413git2f6dcb5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue May 29 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.1.0-5.20180413git2f6dcb5
- Fix Requires

* Mon May 28 2018 Dennis Gilmore <dennis@ausil.us> - 1.1.0-4.20180413git2f6dcb5
- Add back the correct requiresso that the data sub package gets pulled in

* Mon May 28 2018 Dennis Gilmore <dennis@ausil.us> - 1.1.0-3.20180413git2f6dcb5
- remove requires that prevents installation

* Thu Apr 19 2018 Gwyn Ciesla <limburgher@gmail.com> - 1.1.0-2.20180413git2f6dcb5
- Spec corrections.
- Split out data subpackage.

* Fri Apr 13 2018 Gwyn Ciesla <limburgher@gmail.com> - 1.1.0-1
- Adapt to modern packaging guidelines.

* Mon Mar 19 2018 jk@lutty.net
- Initial package derived from mediatomb (fedora) annd gerbera (Suse)
