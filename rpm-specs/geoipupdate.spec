%bcond_without check

# https://github.com/maxmind/geoipupdate
%global goipath	github.com/maxmind/geoipupdate
Version:	4.3.0

%gometa

Name:		geoipupdate
Release:	1%{?dist}
Summary:	Update GeoIP2 binary databases from MaxMind

License:	ASL 2.0 or MIT
URL:		http://dev.maxmind.com/geoip/geoipupdate/
Source0:	%{gosource}
Source1:	geoipupdate.cron

BuildRequires:	coreutils
BuildRequires:	crontabs
BuildRequires:	golang(github.com/gofrs/flock)
# Wants golang(github.com/pkg/errors) ≥ 0.9.1 but seems to work OK with earlier versions
BuildRequires:	golang(github.com/pkg/errors)
BuildRequires:	golang(github.com/spf13/pflag)
BuildRequires:	make
BuildRequires:	pandoc
BuildRequires:	perl-interpreter
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
BuildRequires:	sed
# Legacy databases fetched by cron6 sub-package no longer available
Obsoletes:	geoipupdate-cron6 < %{version}-%{release}

%if %{with check}
# Tests
BuildRequires:	golang(github.com/stretchr/testify/assert)
BuildRequires:	golang(github.com/stretchr/testify/require)
%endif

%description
The GeoIP Update program performs automatic updates of GeoIP2 binary databases.

%package cron
Summary:	Cron job to do weekly updates of GeoIP databases
BuildArch:	noarch
Requires:	%{name} = %{version}-%{release}
Requires:	crontabs
Obsoletes:	GeoIP-update < 1.6.0
Provides:	GeoIP-update = 1.6.0

%description cron
Cron job for weekly updates to GeoIP2 binary databases from MaxMind.

%prep
%goprep

%build
export LDFLAGS='-X main.defaultConfigFile=%{_sysconfdir}/GeoIP.conf -X main.defaultDatabaseDirectory=%{_datadir}/GeoIP '
%gobuild -o %{gobuilddir}/bin/geoipupdate %{goipath}/cmd/geoipupdate

# Work around hardcoded "build" path in dev-bin/make-man-pages.pl
ln -s %{gobuilddir} build

# Prepare the config files and documentation
make BUILDDIR=%{gobuilddir} CONFFILE=%{_sysconfdir}/GeoIP.conf DATADIR=%{_datadir}/GeoIP data

%install
# Install the geoipupdate program
install -d %{buildroot}%{_bindir}
install -p -m 0755 %{gobuilddir}/bin/geoipupdate %{buildroot}%{_bindir}/geoipupdate

# Install the configuration file
# By default we just use the free GeoIP2 databases
install -d %{buildroot}%{_sysconfdir}
install -p -m 0644 conf/GeoIP.conf.default %{buildroot}%{_sysconfdir}/GeoIP.conf

# Ensure the GeoIP data directory exists
# Note: not using %%ghost files for default databases to avoid issues when co-existing with the geolite2 package
install -d %{buildroot}%{_datadir}/GeoIP

# Install the cron script for fetching weekly updates
install -D -m 755 %{SOURCE1} %{buildroot}%{_sysconfdir}/cron.weekly/geoipupdate

# Install the manpages
install -d %{buildroot}%{_mandir}/man1
install -p -m 0644 _build/geoipupdate.1 %{buildroot}%{_mandir}/man1/geoipupdate.1
install -d %{buildroot}%{_mandir}/man5
install -p -m 0644 _build/GeoIP.conf.5 %{buildroot}%{_mandir}/man5/GeoIP.conf.5

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE-APACHE LICENSE-MIT
%doc conf/GeoIP.conf.default README.md CHANGELOG.md
%doc doc/GeoIP.conf.md doc/geoipupdate.md
%config(noreplace) %{_sysconfdir}/GeoIP.conf
%{_bindir}/geoipupdate
%dir %{_datadir}/GeoIP/
%{_mandir}/man1/geoipupdate.1*
%{_mandir}/man5/GeoIP.conf.5*

%files cron
%config(noreplace) %{_sysconfdir}/cron.weekly/geoipupdate

%changelog
* Fri Apr 17 2020 Paul Howarth <paul@city-fan.org> - 4.3.0-1
- Update to 4.3.0
  - First release to Docker Hub (GH#24)
  - The binary builds are now built with CGO_ENABLED=0 (GH#63)

* Mon Feb 24 2020 Paul Howarth <paul@city-fan.org> - 4.2.2-1
- Update to 4.2.2
  - The major version of the module is now included at the end of the module
    path; previously, it was not possible to import the module in projects that
    were using Go modules (GH#81)
  - A valid account ID and license key combination is now required for database
    downloads, so those configuration options are now required
  - The error handling when closing a local database file would previously
    ignore errors and, upon upgrading to 'github.com/pkg/errors' 0.9.0, would
    fail to ignore expected errors (GH#69, GH#70)
  - The RPM release was previously lacking the correct owner and group on files
    and directories: among other things, this caused the package to conflict
    with the 'GeoIP' package in CentOS 7 and 'GeoIP-GeoLite-data' in CentOS 8;
    the files are now owned by 'root' (GH#76)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Nov 10 2019 Paul Howarth <paul@city-fan.org> - 4.1.5-1
- Update to 4.1.5
  - Respect the defaultConfigFile and defaultDatabaseDirectory variables in the
    main package again; they were ignored in 4.1.0 through 4.1.4 (if not
    specified, the GitHub and PPA releases for these versions used the config
    /usr/local/etc/GeoIP.conf instead of /etc/GeoIP.conf and the database
    directory /usr/local/share/GeoIP instead of /usr/share/GeoIP)

* Fri Nov  8 2019 Paul Howarth <paul@city-fan.org> - 4.1.4-1
- Update to 4.1.4
  - Improve man page formatting and organization (GH#44)
  - Provide update functionality as an importable package as well as a
    standalone program (GH#48)
  - Remove formatting, linting, and testing from the geoipupdate target in the
    Makefile

* Sat Sep 14 2019 Paul Howarth <paul@city-fan.org> - 4.0.6-1
- Update to 4.0.6
  - Ignore errors when syncing file system: these errors were primarily due to
    the file system not supporting the sync call (GH#37)
  - Use CRLF line endings on Windows for text files
  - Fix tests on Windows
  - Improve man page formatting (GH#38)
  - Dependencies are no longer vendored (GH#39)

* Sun Sep  1 2019 Paul Howarth <paul@city-fan.org> - 4.0.4-1
- Update to 4.0.4
  - Do not try to sync the database directory when running on Windows; syncing
    this way is not supported there and would lead to an error (GH#32)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 4.0.3-2
- Update to latest Go macros

* Mon Jun 10 2019 Paul Howarth <paul@city-fan.org> - 4.0.3-1
- Update to 4.0.3
  - Update flock dependency from 'theckman/go-flock' to 'gofrs/flock' (GH#22)
  - Switch to Go modules and update dependencies
  - Fix version output on Ubuntu PPA and Homebrew releases
- Revert switch to Go Modules as our tooling isn't ready for that yet

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 18 2019 Paul Howarth <paul@city-fan.org> - 4.0.2-1
- Update to 4.0.2
  - Completely rewritten in the go language
  - New version licensed ASL 2.0 or MIT rather than GPLv2
- Legacy databases no longer available, so drop/obsolete the cron6
  sub-package

* Tue Sep 11 2018 Paul Howarth <paul@city-fan.org> - 3.1.1-1
- Update to 3.1.1
  - Allow parsing of license keys longer than 12 characters

* Fri Aug 17 2018 Paul Howarth <paul@city-fan.org> - 3.1.0-1
- Update to 3.1.0
  Changes in version 3.0.0:
  - BREAKING CHANGE: When downloading the free databases without a MaxMind
    account, you must either not have 'AccountID', 'UserId', or 'LicenseKey'
    set in your configuration file or they must be set to the zero values
    previously recommended in our documentation; any other value will cause an
    authorization error
  - BREAKING CHANGE: The configuration options 'Protocol',
    'SkipPeerVerification', and `SkipHostnameVerification` are no longer
    supported; if they are present in the configuration file, they will be
    ignored - HTTPS with peer and hostname verification will be used on all
    requests
  - BREAKING CHANGE: The configuration file must have the 'AccountID' or the
    deprecated 'UserId' when downloading a paid database; previously, when
    downloading the GeoIP Legacy Country database, you were able to only
    provide the 'LicenseKey'
  - IMPORTANT: 'geoipupdate-pureperl.pl' has been removed and will no longer be
    distributed with 'geoipupdate'; this Perl script had known issues and did
    not have feature parity with the C implementation
  - This program no longer uses the following endpoints:
    '/app/update_getipaddr', '/app/update', and '/app/update_secure';
    '/geoip/databases/{edition_id}/update' is now used instead
  - Fixed issue in 'gu_strnlen()' dereferencing a pointer before checking that
    it was in array bounds
  - We now update the default GeoIP.conf during installation so that directory
    paths match build parameters; previously this config always said the data
    directory was under /usr/local/share which was not always accurate
  - Improve the error checking and display the underlying reason for the error
    when possible (GH#82)
  - Document that the 'LockFile' is not removed from the filesystem after a
    successful exit from the program (GH#79)
  - Make default configuration directory agree with default installation
    directory
  Changes in version 3.0.1:
  - When there were no updates available, 3.0.0 incorrectly returned an exit
    code of 1 instead of 0; this release reverts to the pre-3.0.0 behavior,
    returning an exit code of 0 in this case
  Changes in version 3.1.0:
  - This version restores the ability to use the 'AccountID'/'UserId' 999999
    along with an all-zero license key when downloading free databases;
    however, the use of this combination is not recommended and may break in
    future versions
  - When printing verbose output, only the first four characters of the
    'LicenseKey' will now be displayed

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Oct 31 2017 Paul Howarth <paul@city-fan.org> - 2.5.0-1
- Update to 2.5.0
  - Replace use of strnlen() due to lack of universal availability (GH#71)
  - Document the 'LockFile' option in the 'GeoIP.conf' man page (GH#64)
  - Remove unused base64 library (GH#68)
  - Add the new configuration option 'PreserveFileTimes'; if set, the
    downloaded files will get the same modification times as their original on
    the server (default is '0') (GH#63)
  - Use the correct types when calling 'curl_easy_setopt()'; this fixes
    warnings generated by libcurl's 'typecheck-gcc.h' (GH#61)
  - In 'GeoIP.conf', the 'UserId' option was renamed to 'AccountID' and the
    'ProductIds' option was renamed to 'EditionIDs'; the old options will
    continue to work, but upgrading to the new names is recommended for
    forward compatibility

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri May 26 2017 Paul Howarth <paul@city-fan.org> - 2.4.0-1
- Update to 2.4.0
  - geoipupdate now checks that the database directory is writable: if it is
    not, it reports the problem and aborts
  - geoipupdate now acquires a lock when starting up to ensure only one
    instance may run at a time: a new option, 'LockFile', exists to set the
    file to use as a lock ('.geoipupdate.lock' in the database directory by
    default)
  - geoipupdate now prints out additional information from the server when a
    download request results in something other than HTTP status 2xx; this
    provides more information when the API does not respond with a database
    file
  - ${datarootdir}/GeoIP is now created on 'make install' (GH#29)
  - Previously, a variable named 'ERROR' was used, which caused issues building
    on Windows (GH#36)
- Drop EL-5 support
  - Drop BuildRoot: and Group: tags
  - Drop explicit buildroot cleaning in %%install section
  - Drop explicit %%clean section
  - noarch subpackages always available now
  - libcurl-devel always available now

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan  5 2017 Paul Howarth <paul@city-fan.org> - 2.3.1-1
- Update to 2.3.1
  - geoipupdate now uses TCP keep-alive when compiled with cURL 7.25 or
    greater
  - Previously, on an invalid gzip file, geoipupdate would output binary data
    to stderr; it now displays an appropriate error message
  - Install README, ChangeLog, GeoIP.conf.default etc. into docdir (GH#33)
  - $(sysconfdir) is now created if it doesn't exist (GH#33)
  - The sample config file is now usable (GH#33)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 22 2016 Paul Howarth <paul@city-fan.org> - 2.2.2-1
- Update to 2.2.2
  - geoipupdate now calls fsync on the database directory after a rename to
    make it durable in the event of a crash
- Update autotools patch

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Apr 13 2015 Paul Howarth <paul@city-fan.org> - 2.2.1-2
- Split patch for upstream issue #26 into separate patches for upstream changes
  and effect of running autotools

* Wed Mar  4 2015 Philip A. Prindeville <philipp@fedoraproject.org> - 2.2.1-1
- Update to 2.2.1
  - geoipupdate now verifies the MD5 of the new database before deploying it;
    if the database MD5 does not match the expected MD5, geoipupdate will exit
    with an error
  - The copy of 'base64.c' and 'base64.h' was switched to a version under
    GPLv2+ to prevent a license conflict
  - The 'LICENSE' file was added to the distribution
  - Several issues in the documentation were fixed
- Use interim fix for upstream issue #26 until it's accepted:
  https://github.com/maxmind/geoipupdate/issues/26
- Add buildroot and clean, BR: curl-devel rather than libcurl-devel for
  EL-5 compatibility

* Tue Feb 10 2015 Paul Howarth <paul@city-fan.org> - 2.1.0-4
- New geoipupdate6 cron script written in Perl that doesn't download the data
  if it hasn't changed

* Fri Feb  6 2015 Paul Howarth <paul@city-fan.org> - 2.1.0-3
- Add cron6 subpackage, equivalent to old GeoIP-update6 package
- Revise obsoletes/provides

* Sun Feb  1 2015 Philip A. Prindeville <philipp@fedoraproject.org> - 2.1.0-2
- Remove architecture-specific dependency in noarch subpackage

* Mon Jan 26 2015 Philip A. Prindeville <philipp@fedoraproject.org> - 2.1.0-1
- Initial review package (generated by rpmdev-newspec)

