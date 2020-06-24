# There are various assertion failures with wxGTK3 which need to be investigated
%bcond_with wxGTK3

%if %{with wxGTK3}
%global wx_pkg wxGTK3-devel
%global wx_ver 3.0
%else
%global wx_pkg compat-wxGTK3-gtk2-devel
%global wx_ver 3.0
%endif

%global commit 705eb1b9ee3b1b8ca48d729dbe2def1ae0d3a743
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Summary:	Graphical client for PostgreSQL
Name:		pgadmin3
Version:	1.23.0
Release:	0.1.git%{shortcommit}%{?dist}
License:	PostgreSQL
# Originally http://www.pgadmin.org/, switch to fork with current PG support
URL:            https://github.com/AbdulYadi/pgadmin3
Source:		https://github.com/AbdulYadi/pgadmin3/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Source1:	pgadmin3.appdata.xml
Source2:	pgadmin3.xpm

# Unbundle libssh2
Patch0:         pgadmin3_unbundle-libssh.patch
# Adapt SSL test to pass with OpenSSL 1.1
Patch1:         pgadmin3_openssl11.patch
# Don't remove -g from CFLAGS
Patch2:         pgadmin3_debuginfo.patch
# Fix GCC10 FTBFS: (-Wnarrowing)
Patch3:         pgadmin3_gcc10.patch
# Fix crash on startup
# https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=843774
Patch4:         pgadmin3_startup-crash.patch
# Use a more readable icon
Patch5:         pgadmin3_icon.patch
# Fix data view on High-DPI screens (from pgadmin-hacker list)
Patch6:         pgadmin3_row-heights.patch


BuildRequires:  autoconf automake libtool
BuildRequires:  gcc-c++
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  libpq-devel
BuildRequires:  libssh2-devel
BuildRequires:  libxml2-devel
BuildRequires:  libxslt-devel
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  postgresql-server-devel
BuildRequires:  python3-sphinx
BuildRequires:  %{wx_pkg}
#compat-openssl10-devel


%description
pgAdmin III is a powerful administration and development
platform for the PostgreSQL database, free for any use.
It is designed to answer the needs of all users,
from writing simple SQL queries to developing complex
databases. The graphical interface supports all PostgreSQL
features and makes administration easy.

pgAdmin III is designed to answer the needs of all users,
from writing simple SQL queries to developing complex databases.
The graphical interface supports all PostgreSQL features and
makes administration easy. The application also includes a syntax
highlighting SQL editor, a server-side code editor, an
SQL/batch/shell job scheduling agent, support for the Slony-I
replication engine and much more. No additional drivers are
required to communicate with the database server.

%prep
%autosetup -p1 -n %{name}-%{commit}
# remove embedded libssh2
rm -rf pgadmin/libssh2 pgadmin/include/libssh2


%build
./bootstrap
#export CXXFLAGS="%optflags -fno-delete-null-pointer-checks -Wno-unused-local-typedefs"
%configure --with-wx-version=%{wx_ver}
%make_build


%install
%make_install

# Install icon
install -Dpm 0644 %{SOURCE2} %{buildroot}/%{_datadir}/%{name}/%{name}.xpm

# Install desktop file
mkdir -p %{buildroot}/%{_datadir}/applications
desktop-file-install --dir %{buildroot}%{_datadir}/applications --add-category Development pkg/%{name}.desktop

# Install appdata file
install -Dpm 0644 %{SOURCE1} %{buildroot}%{_metainfodir}/org.postgresql.pgadmin3.appdata.xml

# Install proper docs through %%doc below
rm -rf %{buildroot}%{_datadir}/%{name}/docs

# Properly install locales
mkdir -p %{buildroot}%{_datadir}/locale
rm -f %{buildroot}%{_datadir}/%{name}/i18n/{*,.}/wxstd.mo
mv -f %{buildroot}%{_datadir}/%{name}/i18n/??_?? %{buildroot}%{_datadir}/locale

%find_lang %{name}



%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.postgresql.pgadmin3.appdata.xml


%files -f %{name}.lang
%doc BUGS CHANGELOG LICENSE README.md docs/en_US/_build/htmlhelp/
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_metainfodir}/org.postgresql.pgadmin3.appdata.xml


%changelog
* Thu Apr 09 2020 Sandro Mani <manisandro@gmail.com> - 1.23.0-0.1.git705eb1b
- Switch to maintained fork with PG12 support
- Cleanup packaging

* Mon Mar 09 2020 Sandro Mani <manisandro@gmail.com> - 1.22.2-18
- Fix data view on High-DPI screens

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 14 2019 Jeff Law <law@redhat.com> - 1.22.2-16
- Fix narrowing conversion problem caught by gcc-10

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Mar 15 2019 Sandro Mani <manisandro@gmail.com> - 1.22.2-14
- Add PG11 support
- Build with wxWidgets 3.0 and gtk2 compatibility also on F30+ unless explicitly requested

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 19 2018 Stuart Gathman <stuart@gathman.org> - 1.22.2-12
- Generate larger icon from
- https://www.postgresql.org/media/img/about/press/elephant.png

* Wed Dec 19 2018 Stuart Gathman <stuart@gathman.org> - 1.22.2-11
- Add appdata

* Thu Nov 08 2018 Scott Talbert <swt@techie.net> - 1.22.2-10
- Restore missing patch for PG10
- Build with wxWidgets 3.0 on F30+ only
- Build with wxWidgets 3.0 and gtk2 compatibility on F27-F29

* Wed Nov 07 2018 Scott Talbert <swt@techie.net> - 1.22.2-9
- Rebuild with wxWidgets 3.0

* Tue Nov 06 2018 Scott Talbert <swt@techie.net> - 1.22.2-8
- Adjust BRs to fix FTBFS	

* Tue Nov 06 2018 Stuart Gathman <stuart@gathman.org> - 1.22.2-7
- Build against compat-openssl10	Sandro Mani <manisandro@gmail.com>
- Fix failure to use EVP_CIPHER_CTX_new() 
- Fix broken pgadmin3-nullthis.patch
- Add patch for PG10 support

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Nov 11 2016 Devrim Gündüz <devrim@gunduz.org> 1.22.2-1
- Update to 1.22.2 -- the final release of pgadmin3
- Update patch3

* Tue Aug 23 2016 Stuart Gathman <stuart@gathman.org> 1.22.1-3
- Fix a few of the null pointer problems, bz#1369520

* Tue Jul 19 2016 Stuart Gathman <stuart@gathman.org> 1.22.1-2
- Compile with --no-delete-null-pointer-checks, bz#1335043

* Fri Jul  1 2016 Stuart Gathman <stuart@gathman.org> 1.22.1-1.3
- Attempt to mitigate pervasive this == 0 coding error

* Wed Feb 17 2016 Devrim Gündüz <devrim@gunduz.org> 1.22.1-1
- Update to 1.22.1
- Update download URL

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.20.0-2
- Rebuilt for GCC 5 C++11 ABI change

* Tue Mar 10 2015 Kevin Fenzi <kevin@scrye.com> 1.20.0-1
- Rebuild for new gcc

* Mon Dec 22 2014 Devrim Gündüz <devrim@gunduz.org> 1.20.0-1
- Update to 1.20.0
- Update download URL -- community will deprecate FTP service.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.18.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.18.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Oct 8 2013 Devrim Gündüz <devrim@gunduz.org> 1.18.1-1
- Update to 1.18.1

* Wed Sep 11 2013 Devrim Gündüz <devrim@gunduz.org> 1.18.0-1
- Update to 1.18.0
- Trim changelog

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.16.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jan 25 2013 Devrim Gündüz <devrim@gunduz.org> 1.16.1-1
- Update to 1.16.1

* Mon Oct 29 2012 Devrim Gündüz <devrim@gunduz.org> 1.16.0-2
- Update licence, per bz #871183.

* Sun Oct 28 2012 Devrim Gündüz <devrim@gunduz.org> 1.16.0-1
- Update to 1.16.0

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri May 11 2012 Ville Skyttä <ville.skytta@iki.fi> - 1.14.2-2
- Fix -debuginfo (#746349).

* Thu May 10 2012 Devrim Gündüz <devrim@gunduz.org> 1.14.2-1
- Update to 1.14.2

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Oct 13 2011 Devrim Gündüz <devrim@gunduz.org> 1.14.0-1
- Update to 1.14.0

* Tue Apr 19 2011 Devrim Gündüz <devrim@gunduz.org> 1.12.3-1
- Update to 1.12.3

* Wed Feb 23 2011 Devrim Gündüz <devrim@gunduz.org> 1.12.2-3
- Actually install desktop file.

* Tue Feb 15 2011 Devrim Gündüz <devrim@gunduz.org> 1.12.2-2
- Update to 1.12.2

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Aug 3 2010 Devrim Gündüz <devrim@gunduz.org> 1.10.5-1
- Update to 1.10.5

* Wed Jul 14 2010 Dan Horák <dan@danny.cz> - 1.10.3-3
- rebuilt against wxGTK-2.8.11-2

* Tue Jun 15 2010 Michel Salim <salimma@fedoraproject.org> - 1.10.3-2
- Ship the hints files (bz #513039)

* Thu May 13 2010 Devrim Gündüz <devrim@gunduz.org> 1.10.3-1
- Update to 1.10.3

* Mon Mar 15 2010 Devrim Gündüz <devrim@gunduz.org> 1.10.2-1
- Update to 1.10.2

* Thu Dec 3 2009 Devrim Gündüz <devrim@gunduz.org> 1.10.1-1
- Update to 1.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 29 2009 Devrim Gündüz <devrim@gunduz.org> 1.10.0-1
- Update to 1.10.0
- Update licence
- Incorporate some changes from rpmfusion:
  Corrected pgadmin3 documentation path to avoid errors (#448)
  Re-added the branding directory for some users (RHBZ #473748)
  Removed useless -docs package, main package shipped it anyway
  Many spec file and package cleanups to get rpmlint very silent
