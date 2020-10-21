# Fedora spec initially based on upstream spec file from OBS:
# https://build.opensuse.org/package/view_file/devel:openQA/openQA/openQA.spec
# License: GPLv2+

# openQA has a bunch of private modules (most namespaced but a couple
# not), we do not want automatic provides or requires for these
# ref https://fedoraproject.org/wiki/Packaging:AutoProvidesAndRequiresFiltering#Perl
# but per https://fedorahosted.org/fpc/ticket/591 , these have been
# improved, and contrary to the wiki it is safe to set them first and
# then call perl_default_filter, the values will be properly merged.
# I tried to sell upstream on naming these properly and installing
# them to the perl vendor dir, but they wouldn't bite:
# https://github.com/os-autoinst/os-autoinst/issues/387
# Despite the apparently-CPAN-like name, DBIx::Class::Timestamps is
# installed to openQA's private directory and should be excluded.
# perl(Perl::Critic) requirements come from HashKeyQuotes.pm, which is
# used only for tests, so we don't want a runtime requirement.

%global __provides_exclude_from %{_datadir}/openqa/lib
%global __requires_exclude perl\\((OpenQA|DBIx::Class::Timestamps|MojoDebugHandle|db_helpers|db_profiler|Perl::Critic)
%{?perl_default_filter}

%global github_owner    os-autoinst
%global github_name     openQA
%global github_version  4.6
%global github_commit   e9b44740c89522368b2561bf94a34d86d11eb62d
# if set, will be a post-release snapshot build, otherwise a 'normal' build
%global github_date     20200805
%global shortcommit     %(c=%{github_commit}; echo ${c:0:7})

# can't use linebreaks here!
%global openqa_services openqa-webui.service openqa-gru.service openqa-websockets.service openqa-scheduler.service openqa-enqueue-audit-event-cleanup.service openqa-enqueue-audit-event-cleanup.timer openqa-enqueue-asset-cleanup.service openqa-enqueue-asset-cleanup.timer openqa-enqueue-result-cleanup.service openqa-enqueue-result-cleanup.timer openqa-enqueue-bug-cleanup.service openqa-enqueue-bug-cleanup.timer
%global openqa_worker_services openqa-worker.target openqa-slirpvde.service openqa-vde_switch.service openqa-worker-cacheservice.service openqa-worker-cacheservice-minion.service

%if %{undefined tmpfiles_create}
%global tmpfiles_create() \
%{_bindir}/systemd-tmpfiles --create %{?*} >/dev/null 2>&1 || :
%{nil}
%endif

%define python_scripts_requires python3-requests python3-future

# The following line is generated from dependencies.yaml (upstream)
%define assetpack_requires perl(CSS::Minifier::XS) >= 0.01 perl(JavaScript::Minifier::XS) >= 0.11 perl(Mojolicious::Plugin::AssetPack) >= 1.36
# The following line is generated from dependencies.yaml (upstream)
%define common_requires perl(Archive::Extract) > 0.7 perl(Config::IniFiles) perl(Cpanel::JSON::XS) perl(Cwd) perl(Data::Dump) perl(Data::Dumper) perl(Digest::MD5) perl(Getopt::Long) perl(Minion) >= 10.08 perl(Mojolicious) >= 8.55 perl(Regexp::Common) perl(Storable) perl(Try::Tiny)
# runtime requirements for the main package that are not required by other sub-packages
# The following line is generated from dependencies.yaml (upstream)
%define main_requires %assetpack_requires git-core perl(BSD::Resource) perl(Carp) perl(Carp::Always) perl(CommonMark) perl(Config::Tiny) perl(DBD::Pg) >= 3.7.4 perl(DBI) >= 1.632 perl(DBIx::Class) >= 0.082801 perl(DBIx::Class::DeploymentHandler) perl(DBIx::Class::DynamicDefault) perl(DBIx::Class::OptimisticLocking) perl(DBIx::Class::ResultClass::HashRefInflator) perl(DBIx::Class::Schema::Config) perl(DBIx::Class::Storage::Statistics) perl(Date::Format) perl(DateTime) perl(DateTime::Duration) perl(DateTime::Format::Pg) perl(Exporter) perl(Fcntl) perl(File::Basename) perl(File::Copy) perl(File::Copy::Recursive) perl(File::Path) perl(File::Spec) perl(FindBin) perl(Getopt::Long::Descriptive) perl(IO::Handle) perl(IPC::Run) perl(JSON::Validator) perl(LWP::UserAgent) perl(Module::Load::Conditional) perl(Module::Pluggable) perl(Mojo::Base) perl(Mojo::ByteStream) perl(Mojo::IOLoop) perl(Mojo::JSON) perl(Mojo::Pg) perl(Mojo::RabbitMQ::Client) >= 0.2 perl(Mojo::URL) perl(Mojo::Util) perl(Mojolicious::Commands) perl(Mojolicious::Plugin) perl(Mojolicious::Static) perl(Net::OpenID::Consumer) perl(POSIX) perl(Pod::POM) perl(SQL::Translator) perl(Scalar::Util) perl(Sort::Versions) perl(Text::Diff) perl(Time::HiRes) perl(Time::ParseDate) perl(Time::Piece) perl(Time::Seconds) perl(URI::Escape) perl(YAML::PP) >= 0.020 perl(YAML::XS) perl(aliased) perl(base) perl(constant) perl(diagnostics) perl(strict) perl(warnings)
# The following line is generated from dependencies.yaml (upstream)
%define client_requires curl git-core jq perl(Getopt::Long::Descriptive) perl(IO::Socket::SSL) >= 2.009 perl(IPC::Run) perl(JSON::Validator) perl(LWP::Protocol::https) perl(LWP::UserAgent) perl(Test::More) perl(YAML::PP) >= 0.020 perl(YAML::XS)
# diff from SUSE: case (they have openQA-client, we have openqa-client)
# The following line is generated from dependencies.yaml (upstream)
%define worker_requires openqa-client optipng os-autoinst < 5 perl(Minion::Backend::SQLite) >= 5.0.1 perl(Mojo::IOLoop::ReadWriteProcess) >= 0.26 perl(Mojo::SQLite)
# The following line is generated from dependencies.yaml (upstream)
%define build_requires %assetpack_requires rubygem(sass)

# All requirements needed by the tests executed during build-time.
# Do not require on this in individual sub-packages except for the devel
# package.
# Diff from SUSE: Selenium requirements dropped as not available in Fedora,
# critic, (python) yamllint and (python) jsbeautify requirements dropped
# (except Perl::Critic itself as the compile-check-all test fails on the
# in-tree critic module if we leave that out) as we don't run those checks
# in our package build (SUSE runs them in theirs)
# The following line is generated from dependencies.yaml (upstream)
%define test_requires %common_requires %main_requires %python_scripts_requires %worker_requires ShellCheck curl jq os-autoinst-devel perl(App::cpanminus) perl(Mojolicious::Plugin::OAuth2) perl(Perl::Critic) perl(Test::Exception) perl(Test::Fatal) perl(Test::MockModule) perl(Test::MockObject) perl(Test::Mojo) perl(Test::Most) perl(Test::Output) perl(Test::Pod) perl(Test::Strict) perl(Test::Warnings) >= 0.029 postgresql-server
%ifarch x86_64
%define qemu qemu qemu-kvm
%else
%define qemu qemu
%endif
# diff from SUSE: perl(Devel::Cover::Report::Codecov) dropped because
# it's not in Fedora (this means you can't run 'make coverage-codecov')
# xorg-x11-fonts dropped because that binary package doesn't exist in
# Fedora (it exists as a source package generating multiple binary
# packages) and I can't find any particular reason for it
# The following line is generated from dependencies.yaml (upstream)
%define devel_requires %build_requires %qemu %test_requires curl perl(Devel::Cover) perl(Perl::Tidy) postgresql-devel rsync sudo tar
%define devel_no_selenium_requires %build_requires %qemu %test_requires curl perl(Devel::Cover) perl(Perl::Tidy) postgresql-devel rsync sudo tar
# diff from SUSE: chromedriver dropped as we don't package it
# that makes this look fairly silly, but we want to follow the SUSE
# spec as close as we can
# The following line is generated from dependencies.yaml (upstream)
%define devel_requires %devel_no_selenium_requires

Name:           openqa
Version:        %{github_version}
Release:        54%{?github_date:.%{github_date}git%{shortcommit}}%{?dist}
Summary:        OS-level automated testing framework
License:        GPLv2+
Url:            http://os-autoinst.github.io/openQA/
Source0:        https://github.com/%{github_owner}/%{github_name}/archive/%{github_commit}/%{github_name}-%{github_commit}.tar.gz
# pre-generated cached assets, build with update-cache.sh. We could
# install without these and let openQA generate them at run time, but
# we don't for two reasons: we don't want to let a webapp rewrite
# itself if avoidable (it's a security risk), and the tests don't work
# without the asset cache present. This should be re-generated any
# time Source0 changes.
Source1:        assetcache-%{github_commit}.tar.xz
# Plugin to restart failed update tests (to avoid spurious failures)
# FIXME: this probably doesn't handle jobs with parents/children
# properly
Source2:        FedoraUpdateRestart.pm
# fedora-messaging publishing plugin (upstream doesn't want this as
# it's too fedora-y for them)
Source3:        FedoraMessaging.pm
# tests for the fedora-messaging publishing plugin
Source4:        23-fedora-messaging.t

# Fix a weird perl lib path issues that breaks the tests in Fedora build env
# https://github.com/os-autoinst/openQA/pull/3302
Patch0:         0001-make-test-with-database-add-I-PWD-t-lib-back-to-PERL.patch

BuildRequires:  %{python_scripts_requires}
BuildRequires:  perl-generators
# Standard for packages that have systemd services
BuildRequires:  systemd
# Build and tests need LC_ALL=en_US.UTF-8, so we need this...
BuildRequires:  glibc-langpack-en
BuildRequires:  %{build_requires}
BuildRequires:  %{test_requires}
Requires:       perl(Minion) >= 10.0
Requires:       %{main_requires}
Requires:       openqa-common = %{version}-%{release}
Requires:       openqa-client = %{version}-%{release}
Requires(post): coreutils

# Standard for packages that have systemd services
%{?systemd_requires}

# the plugin is needed if the auth method is set to "oauth2"
Recommends:     perl(Mojolicious::Plugin::OAuth2)
# server needs to run an rsync server if worker caching is used
Recommends:     rsync

# For the httpd subpackage split in 4.3-7, needed for updates to work right
Obsoletes:      openqa < 4.3-7

BuildArch:      noarch

%description
openQA is a testing framework that allows you to test GUI applications on one
hand and bootloader and kernel on the other. In both cases, it is difficult to
script tests and verify the output. Output can be a popup window or it can be
an error in early boot even before init is executed.

openQA is an automated test tool that makes it possible to test the whole
installation process of an operating system. It uses virtual machines to
reproduce the process, check the output (both serial console and screen) in
every step and send the necessary keystrokes and commands to proceed to the
next. openQA can check whether the system can be installed, whether it works
properly in 'live' mode, whether applications work or whether the system
responds as expected to different installation options and commands.

Even more importantly, openQA can run several combinations of tests for every
revision of the operating system, reporting the errors detected for each
combination of hardware configuration, installation options and variant of the
operating system.

%package devel
Summary:        Development package pulling in all build+test dependencies
Requires:       %{devel_requires}

%description devel
Development package pulling in all build+test dependencies.


%package common
Summary:        Common components for openQA server and workers
Requires:       %{common_requires}
# critical bug fix
Requires:       perl(DBIx::Class) >= 0.082801
# assetpack has to approximately match version srpm was built with
Requires:       perl(Mojolicious::Plugin::AssetPack) >= 2.01

%description common
This package contains shared resources for the openQA server and
openQA workers.


%package worker
Summary:        The openQA worker
%define worker_requires_including_uncovered_in_tests %worker_requires perl(SQL::SplitStatement)
Requires:       %{worker_requires_including_uncovered_in_tests}
Requires:       openqa-common = %{version}-%{release}
Requires(post): coreutils
Requires(post): os-autoinst >= 4.6
Recommends:     qemu
# Needed for caching - not required if caching not used...
Recommends:     rsync

Requires(post):     systemd
Requires(preun):    systemd
Requires(postun):   systemd

%description worker
The openQA worker manages the os-autoinst test engine. A system with
openqa-worker installed can run an arbitrary number of openQA workers
(as many as its hardware can support), each of which will run a single
openQA test job at a time, as long as appropriate jobs for the worker
are available from the server it is configured to work for.


%package httpd
Summary:        openQA httpd (Apache) integration
Requires:       httpd
Requires:       httpd-filesystem
# prior to 4.3-7, these files were part of the core package; this is
# here so people who had those versions installed don't lose their
# bits on update
Obsoletes:      openqa < 4.3-7
# Note: does not require any part of openQA as you may wish to have
# Apache and openQA running on different boxes

%description httpd
This package contains httpd (Apache) configuration for the openQA
automated testing framework. openQA runs as a self-contained http
server which is expected to be reverse-proxied by a public-facing http
server (rather than being accessed directly). The config snippets in
this package help you configure openQA to be reverse proxied by httpd.

%package plugin-fedora-messaging
Summary:        openQA plugin for publishing to fedora-messaging
Requires:       openqa >= 4.3-20
Requires:       perl(Digest::SHA)
BuildRequires:  perl(Digest::SHA)
Requires:       perl(UUID::URandom)
BuildRequires:  perl(UUID::URandom)
# Old name
Obsoletes:      %{name}-plugin-fedmsg < 4.7
Provides:       %{name}-plugin-fedmsg = %{version}-%{release}

%description plugin-fedora-messaging
This package contains an openQA plugin which sends fedora-messaging
messages for certain openQA internal events. To enable the plugin, put
'plugins = FedoraMessaging' in the global section of
/etc/openqa/openqa.ini. The plugin piggybacks on the upstream AMQP
plugin, and follows its configuration (in the 'amqp' section of
openqa.ini).

%package plugin-fedoraupdaterestart
Summary:        openQA plugin for restarting failed Fedora update tests
Requires:       openqa

%description plugin-fedoraupdaterestart
This package contains an openQA plugin which restarts update tests that
fail. This is a highly Fedora-specific plugin relying on the flavor
names used for update tests in Fedora. The idea is to re-run failed
tests in case the failure was something transient and unrelated to the
update (network issue, quasi-random bug in underlying package, etc.)

%package client
Summary:        Client tools for remote openQA management
Requires:       openqa-common = %{version}
Requires:       %client_requires

%description client
This package contains the openQA client script, along with several
other useful tools and support files. The client script is a convenient
helper for interacting with the openQA REST API.

%package python-scripts
Summary:        Additional scripts in python
Group:          Development/Tools/Other
Requires:       %python_scripts_requires

%description python-scripts
Additional scripts for the use of openQA in the python programming language.

%package local-db
Summary:        Helper package to ease setup of postgresql DB
Requires:       %name
Requires:       postgresql-server
Supplements:    packageand(%name:postgresql-server)

%description local-db
You only need this package if you have a local postgresql server
next to the webui.

%package single-instance
Summary:        Convenience package for a single-instance setup
Requires:       %{name}-local-db
Requires:       %{name}-worker
Requires:       httpd

%description single-instance
Use this package to setup a local instance with all services provided together.

%package bootstrap
Summary:        Automated openQA setup

%description bootstrap
This can automatically setup openQA - either directly on your system
or within a systemd-nspawn container.

%package doc
Summary:        The openQA documentation

%description doc
Documentation material covering installation, configuration, basic test
writing, etc., covering both openQA and the os-autoinst test engine.

%prep
%autosetup -p1 -n %{github_name}-%{github_commit} -a 1
sed -e 's,/bin/env python,/bin/python,' -i script/openqa-label-all
# Fedora calls it httpd.service, SUSE calls it apache2.service...
sed -i -e 's,apache2\.service,httpd\.service,g' systemd/*.service
# ...Fedora keeps httpd config here, SUSE keeps it there.
sed -i -e 's,"$(DESTDIR)"/etc/apache2/vhosts.d,"$(DESTDIR)"%{_sysconfdir}/httpd/conf.d,g' Makefile
sed -i -e 's,/etc/apache2/vhosts.d,%{_sysconfdir}/httpd/conf.d,g' etc/apache2/vhosts.d/*
# These are the Fedora-y standard TLS cert/key locations.
sed -i -e 's,/etc/apache2/ssl.crt,%{_sysconfdir}/pki/tls/certs,g' etc/apache2/vhosts.d/*
sed -i -e 's,/etc/apache2/ssl.key,%{_sysconfdir}/pki/tls/private,g' etc/apache2/vhosts.d/*
# Add our downstream plugins to the sources
cp %{SOURCE2} lib/OpenQA/WebAPI/Plugin/
cp %{SOURCE3} lib/OpenQA/WebAPI/Plugin/
# we don't really need the tidy test
rm -f t/00-tidy.t
# add the fedora-messaging publishing plugin test to the sources
cp %{SOURCE4} t/


%build
# this does nothing, but it's harmless, so just in case it turns up...
make %{?_smp_mflags}


%install
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
%make_install

mkdir -p %{buildroot}%{_datadir}/openqa/etc/openqa
ln -s %{_sysconfdir}/openqa/openqa.ini %{buildroot}%{_datadir}/openqa/etc/openqa/openqa.ini
ln -s %{_sysconfdir}/openqa/database.ini %{buildroot}%{_datadir}/openqa/etc/openqa/database.ini
mkdir -p %{buildroot}%{_bindir}
ln -s %{_datadir}/openqa/script/client %{buildroot}%{_bindir}/openqa-client
ln -s %{_datadir}/openqa/script/openqa-cli %{buildroot}%{_bindir}/openqa-cli
ln -s %{_datadir}/openqa/script/openqa-clone-job %{buildroot}%{_bindir}/openqa-clone-job
ln -s %{_datadir}/openqa/script/dump_templates %{buildroot}%{_bindir}/openqa-dump-templates
ln -s %{_datadir}/openqa/script/load_templates %{buildroot}%{_bindir}/openqa-load-templates
ln -s %{_datadir}/openqa/script/openqa-clone-custom-git-refspec %{buildroot}%{_bindir}/openqa-clone-custom-git-refspec
ln -s %{_datadir}/openqa/script/openqa-validate-yaml %{buildroot}%{_bindir}/openqa-validate-yaml
ln -s %{_datadir}/openqa/script/setup-db %{buildroot}%{_bindir}/openqa-setup-db
ln -s %{_datadir}/openqa/script/openqa-label-all %{buildroot}%{_bindir}/openqa-label-all


cd %{buildroot}
grep -rl %{_bindir}/env . | while read file; do
    sed -e 's,%{_bindir}/env perl,%{_bindir}/perl,' -i $file
done

mkdir %{buildroot}%{_localstatedir}/lib/openqa/pool/1
mkdir %{buildroot}%{_localstatedir}/lib/openqa/cache
mkdir %{buildroot}%{_localstatedir}/lib/openqa/webui
mkdir %{buildroot}%{_localstatedir}/lib/openqa/webui/cache

# We don't do AppArmor
rm -rf %{buildroot}%{_sysconfdir}/apparmor.d


%check
rm -rf %{buildroot}/DB
export LC_ALL=en_US.UTF-8
# seems necessary to make 24-worker-job.t pass - two subtests there
# rely on one of these files getting uploaded, but that only happens
# if they exist. upstream repo does this in .travis.yml.
touch openqa-debug.log autoinst-log.txt
chmod a+w openqa-debug.log autoinst-log.txt
# we can't use 'unshare' in Fedora package build env
sed -i -e 's,unshare -r -n ,,g' t/40-script_openqa-clone-custom-git-refspec.t t/40-openqa-clone-job.t t/32-openqa_client-script.t
# this test expects a 'not connected' error that it gets with unshare
# but with mock we get 'Connection refused', so just wipe it
sed -i -e '/fails without network/d' t/32-openqa_client-script.t
# Skip tests not working currently, or flaky
rm t/25-cache-service.t t/17-labels_carry_over.t
# XXX for mock builds, uncomment this: see
# https://github.com/rpm-software-management/mock/issues/612
#rm t/40-openqa-clone-job.t

# GIT_CEILING_DIRECTORIES here avoids a case where git error handling
# can differ when you run the build in mock and cause 16-utils-runcmd
# to fail
make test-with-database GIT_CEILING_DIRECTORIES="/" CHECKSTYLE=0 PROVE_ARGS='-l -r' TEST_PG_PATH=%{buildroot}/DB
rm -rf %{buildroot}/DB


%pre
getent group geekotest >/dev/null || groupadd -r geekotest || :
getent passwd geekotest >/dev/null || \
    useradd -r -g geekotest -d /var/lib/openqa -s /sbin/nologin \
    -c "openQA user" geekotest || :

%pre worker
getent group _openqa-worker >/dev/null || groupadd -r _openqa-worker || :
getent passwd _openqa-worker >/dev/null || \
    useradd -r -g _openqa-worker -G qemu -d /dev/null -s /sbin/nologin \
    -c "openQA worker" _openqa-worker || :

%post
%tmpfiles_create %{_tmpfilesdir}/openqa-webui.conf
%systemd_post %{openqa_services}

%post worker
%tmpfiles_create %{_tmpfilesdir}/openqa.conf
%systemd_post %{openqa_worker_services}

%post httpd
if [ $1 -eq 1 ]; then
    echo "### copy and edit /etc/httpd/conf.d/openqa.conf.template!"
fi

%preun
%systemd_preun %{openqa_services}
if [ $1 -eq 0 ]; then
   rm -rf %{_datadir}/openqa/public/packed
fi

%preun worker
%systemd_preun %{openqa_worker_services}

%postun
%systemd_postun_with_restart %{openqa_services}

%postun worker
%systemd_postun_with_restart %{openqa_worker_services}

%post local-db
%systemd_post openqa-setup-db.service

%preun local-db
%systemd_preun openqa-setup-db.service

%postun local-db
%systemd_postun_with_restart openqa-setup-db.service

%files
%doc README.asciidoc
%dir %{_sysconfdir}/openqa
%config(noreplace) %{_sysconfdir}/openqa/openqa.ini
%config(noreplace) %attr(-,root,geekotest) %{_sysconfdir}/openqa/database.ini
%dir %{_datadir}/openqa
%dir %{_datadir}/openqa/etc
%dir %{_datadir}/openqa/etc/openqa
%{_datadir}/openqa/etc/openqa/openqa.ini
%{_datadir}/openqa/etc/openqa/database.ini
%config %{_sysconfdir}/logrotate.d
# init
%{_unitdir}/openqa-webui.service
%{_unitdir}/openqa-livehandler.service
%{_unitdir}/openqa-gru.service
%{_unitdir}/openqa-scheduler.service
%{_unitdir}/openqa-websockets.service
%{_unitdir}/openqa-enqueue-audit-event-cleanup.service
%{_unitdir}/openqa-enqueue-audit-event-cleanup.timer
%{_unitdir}/openqa-enqueue-asset-cleanup.service
%{_unitdir}/openqa-enqueue-asset-cleanup.timer
%{_unitdir}/openqa-enqueue-result-cleanup.service
%{_unitdir}/openqa-enqueue-result-cleanup.timer
%{_unitdir}/openqa-enqueue-bug-cleanup.service
%{_unitdir}/openqa-enqueue-bug-cleanup.timer
%{_tmpfilesdir}/openqa-webui.conf
# web libs
%{_datadir}/openqa/lib/DBIx/
%{_datadir}/openqa/lib/OpenQA/LiveHandler.pm
%{_datadir}/openqa/lib/OpenQA/Resource/
%{_datadir}/openqa/lib/OpenQA/Scheduler/
%{_datadir}/openqa/lib/OpenQA/Schema/
%{_datadir}/openqa/lib/OpenQA/WebAPI/
%{_datadir}/openqa/lib/OpenQA/WebSockets/
%{_datadir}/openqa/templates
%{_datadir}/openqa/public
%{_datadir}/openqa/dbicdh
%{_datadir}/openqa/assets
%dir %{_datadir}/openqa/script
%{_datadir}/openqa/script/configure-web-proxy
%{_datadir}/openqa/script/create_admin
%{_datadir}/openqa/script/fetchneedles
%{_datadir}/openqa/script/initdb
%{_datadir}/openqa/script/openqa
%{_datadir}/openqa/script/openqa-scheduler
%{_datadir}/openqa/script/openqa-scheduler-daemon
%{_datadir}/openqa/script/openqa-websockets
%{_datadir}/openqa/script/openqa-websockets-daemon
%{_datadir}/openqa/script/openqa-livehandler
%{_datadir}/openqa/script/openqa-livehandler-daemon
%{_datadir}/openqa/script/openqa-enqueue-asset-cleanup
%{_datadir}/openqa/script/openqa-enqueue-audit-event-cleanup
%{_datadir}/openqa/script/openqa-enqueue-bug-cleanup
%{_datadir}/openqa/script/openqa-enqueue-result-cleanup
%{_datadir}/openqa/script/openqa-gru
%{_datadir}/openqa/script/openqa-webui-daemon
%{_datadir}/openqa/script/upgradedb
%{_datadir}/openqa/script/modify_needle
%dir %{_localstatedir}/lib/openqa/share
%defattr(-,geekotest,root)
# the database script does creation with 'geekotest' privileges
%dir %{_localstatedir}/lib/openqa/db
# the server may create files in these locations
%dir %{_localstatedir}/lib/openqa/images
%dir %{_localstatedir}/lib/openqa/webui
%dir %{_localstatedir}/lib/openqa/webui/cache
%dir %{_localstatedir}/lib/openqa/share/factory
%dir %{_localstatedir}/lib/openqa/share/tests
%{_localstatedir}/lib/openqa/testresults
# when sqlite is used this file must be server-writable and *not*
# readable by anyone but server or root, hence expected permissions
%ghost %attr(0640,geekotest,root) %{_localstatedir}/lib/openqa/db/db.sqlite

%files devel

%files common
%license COPYING
%dir %{_datadir}/openqa
%ghost %dir %{_datadir}/openqa/packed
%{_datadir}/openqa/lib
%exclude %{_datadir}/openqa/lib/OpenQA/WebAPI/Plugin/FedoraMessaging.pm
%exclude %{_datadir}/openqa/lib/OpenQA/WebAPI/Plugin/FedoraUpdateRestart.pm
%exclude %{_datadir}/openqa/lib/OpenQA/CacheService/
%exclude %{_datadir}/openqa/lib/DBIx/
%exclude %{_datadir}/openqa/lib/OpenQA/Client.pm
%exclude %{_datadir}/openqa/lib/OpenQA/Client
%exclude %{_datadir}/openqa/lib/OpenQA/UserAgent.pm
%exclude %{_datadir}/openqa/lib/OpenQA/LiveHandler.pm
%exclude %{_datadir}/openqa/lib/OpenQA/Resource/
%exclude %{_datadir}/openqa/lib/OpenQA/Scheduler/
%exclude %{_datadir}/openqa/lib/OpenQA/Schema/
%exclude %{_datadir}/openqa/lib/OpenQA/WebAPI/
%exclude %{_datadir}/openqa/lib/OpenQA/WebSockets/
%exclude %{_datadir}/openqa/lib/OpenQA/Worker/
%dir %{_localstatedir}/lib/openqa
# these are compatibility symlinks into the shared data; they go in
# -common because both server and workers need them but they're not in
# the shared location
%{_localstatedir}/lib/openqa/factory
%{_localstatedir}/lib/openqa/tests
# this is a compat symlink to a directory whose contents are split
# between server and worker
%{_localstatedir}/lib/openqa/script

%files worker
%{_datadir}/openqa/lib/OpenQA/CacheService/
%{_datadir}/openqa/lib/OpenQA/Worker/
%config(noreplace) %{_sysconfdir}/openqa/workers.ini
%config(noreplace) %attr(0400,_openqa-worker,root) %{_sysconfdir}/openqa/client.conf
# init
%dir %{_unitdir}
%{_prefix}/lib/systemd/system-generators/systemd-openqa-generator
%{_unitdir}/openqa-worker.target
%{_unitdir}/openqa-worker@.service
%{_unitdir}/openqa-worker-cacheservice-minion.service
%{_unitdir}/openqa-worker-cacheservice.service
%{_unitdir}/openqa-worker-no-cleanup@.service
%{_unitdir}/openqa-slirpvde.service
%{_unitdir}/openqa-vde_switch.service
%{_datadir}/openqa/script/openqa-slirpvde
%{_datadir}/openqa/script/openqa-vde_switch
%{_tmpfilesdir}/openqa.conf
%ghost %dir %{_rundir}/openqa
# worker libs
%dir %{_datadir}/openqa
%dir %{_datadir}/openqa/script
%{_datadir}/openqa/script/worker
%{_datadir}/openqa/script/openqa-workercache
%{_datadir}/openqa/script/openqa-workercache-daemon
%{_datadir}/openqa/script/openqa-worker-cacheservice-minion
%dir %{_localstatedir}/lib/openqa/pool
%defattr(-,_openqa-worker,root)
%dir %{_localstatedir}/lib/openqa/cache
# own one pool - to create the others is task of the admin
%dir %{_localstatedir}/lib/openqa/pool/1

# Note: remote workers are required to mount /var/lib/openqa/share
# shared with the server.

%files httpd
%license COPYING
# apache vhost
%config %{_sysconfdir}/httpd/conf.d/openqa.conf.template
%config %{_sysconfdir}/httpd/conf.d/openqa-common.inc
%config %{_sysconfdir}/httpd/conf.d/openqa-ssl.conf.template

%files client
%dir %{_datadir}/openqa
%dir %{_datadir}/openqa/script
%{_datadir}/openqa/script/client
%{_datadir}/openqa/script/clone_job.pl
%{_datadir}/openqa/script/dump_templates
%{_datadir}/openqa/script/load_templates
%{_datadir}/openqa/script/openqa-cli
%{_datadir}/openqa/script/openqa-clone-job
%{_datadir}/openqa/script/openqa-clone-custom-git-refspec
%{_datadir}/openqa/script/openqa-validate-yaml
%dir %{_datadir}/openqa/lib
%{_datadir}/openqa/lib/OpenQA/Client.pm
%{_datadir}/openqa/lib/OpenQA/Client
%{_datadir}/openqa/lib/OpenQA/UserAgent.pm
%{_bindir}/openqa-client
%{_bindir}/openqa-cli
%{_bindir}/openqa-clone-job
%{_bindir}/openqa-dump-templates
%{_bindir}/openqa-load-templates
%{_bindir}/openqa-clone-custom-git-refspec
%{_bindir}/openqa-validate-yaml

%files python-scripts
%{_datadir}/openqa/script/openqa-label-all
%{_bindir}/openqa-label-all

%files doc
%doc docs/*

%files local-db
%{_unitdir}/openqa-setup-db.service
%{_datadir}/openqa/script/setup-db
%{_bindir}/openqa-setup-db

%files single-instance

%files bootstrap
%{_datadir}/openqa/script/openqa-bootstrap
%{_datadir}/openqa/script/openqa-bootstrap-container

%files plugin-fedora-messaging
%{_datadir}/openqa/lib/OpenQA/WebAPI/Plugin/FedoraMessaging.pm

%files plugin-fedoraupdaterestart
%{_datadir}/openqa/lib/OpenQA/WebAPI/Plugin/FedoraUpdateRestart.pm

%changelog
* Fri Aug 07 2020 Adam Williamson <awilliam@redhat.com> - 4.6-54.20200805gite9b4474
- Fix FedoraUpdateRestart plugin for upstream code change

* Wed Aug 05 2020 Adam Williamson <awilliam@redhat.com> - 4.6-53.20200805gite9b4474
- Bump to latest git, re-sync spec with upstream

* Tue Aug 04 2020 Adam Williamson <awilliam@redhat.com> - 4.6-52.20200607git5349e27
- Bump to more recent git, re-sync spec with upstream

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.6-51.20200429git46234f9
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.6-50.20200429git46234f9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Apr 29 2020 Adam Williamson <awilliam@redhat.com> - 4.6-49.20200429git46234f9
- Bump to latest git
- Resync spec with upstream
- Backport PR #3017: missing asset check shouldn't use 'hidden' asset attribute

* Sat Apr 18 2020 Adam Williamson <awilliam@redhat.com> - 4.6-48.20200415git7160d88
- Backport PR #2955 to fix broken load_templates --clean

* Wed Apr 15 2020 Adam Williamson <awilliam@redhat.com> - 4.6-47.20200415git7160d88
- Bump to latest git
- Drop merged patch
- Resync spec with upstream

* Fri Mar 20 2020 Adam Williamson <awilliam@redhat.com> - 4.6-46.20200319git12cea51
- Backport #2856 to fix extracting compressed download assets

* Thu Mar 19 2020 Adam Williamson <awilliam@redhat.com> - 4.6-45.20200319git12cea51
- Bump to latest git (inc. fix for POO #62417)
- Drop workaround for POO #62417

* Thu Mar 19 2020 Adam Williamson <awilliam@redhat.com> - 4.6-44.20200205git4861e34
- Restart aarch64 install tests that fail in the first module (#1689037)

* Wed Feb 05 2020 Adam Williamson <awilliam@redhat.com> - 4.6-43.20200205git4861e34
- Bump to latest git again (mainly for scheduling fixes)
- Resync spec with upstream
- Tweak restart plugin:
  + Restart FreeIPA jobs (we have the capacity now, and it should work)
  + Restart incomplete jobs (as a hack for POO #62417)

* Wed Feb 05 2020 Adam Williamson <awilliam@redhat.com> - 4.6-42.20200101git68ae00a
- Backport #2667 to fix a scheduling race causing incomplete jobs

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.6-41.20200101git68ae00a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 06 2020 Adam Williamson <awilliam@redhat.com> - 4.6-40.20200101git68ae00a
- Backport #2636 to fix an asset download bug that breaks tests

* Thu Jan 02 2020 Adam Williamson <awilliam@redhat.com> - 4.6-39.20200101git68ae00a
- Bump to latest git again
- Resync with upstream spec
- Update FedoraMessaging plugin for changes to constants

* Fri Nov 22 2019 Adam Williamson <awilliam@redhat.com> - 4.6-38.20191121git8fcf81f
- Drop a couple of unsatisfiable deps from the -devel package

* Thu Nov 21 2019 Adam Williamson <awilliam@redhat.com> - 4.6-37.20191121git8fcf81f
- Update to latest git again

* Tue Nov 05 2019 Adam Williamson <awilliam@redhat.com> - 4.6-36.20191105git09e70da
- Update to latest upstream git
- Drop merged patches

* Fri Nov 01 2019 Adam Williamson <awilliam@redhat.com> - 4.6-35.20191031git127fcf3
- Backport PR #2456 to fix a needle URL issue affecting needle diff

* Thu Oct 31 2019 Adam Williamson <awilliam@redhat.com> - 4.6-34.20191031git127fcf3
- Update to latest upstream git
- Resync spec with upstream
- Drop fedmsg plugin (only carry fedora-messaging now)

* Fri Sep 20 2019 Adam Williamson <awilliam@redhat.com> - 4.6-33.20190806git1c53390
- FedoraMessaging: include NVRs in update messages, change id

* Tue Aug 20 2019 Adam Williamson <awilliam@redhat.com> - 4.6-32.20190806git1c53390
- Backport a patch to fix some annoying log warnings

* Tue Aug 13 2019 Adam Williamson <awilliam@redhat.com> - 4.6-31.20190806git1c53390
- FedoraMessaging: fix fedora_messaging_schema header value

* Fri Aug 09 2019 Adam Williamson <awilliam@redhat.com> - 4.6-30.20190806git1c53390
- Fix test invocation again

* Thu Aug 08 2019 Adam Williamson <awilliam@redhat.com> - 4.6-29.20190806git1c53390
- FedoraMessaging: only include (sub)variant if it's defined

* Thu Aug 08 2019 Adam Williamson <awilliam@redhat.com> - 4.6-28.20190806git1c53390
- Fix FedoraMessaging 'system' value to be an array of hashes

* Thu Aug 08 2019 Adam Williamson <awilliam@redhat.com> - 4.6-27.20190806git1c53390
- Tweak FedoraMessaging update message 'release' data

* Thu Aug 08 2019 Adam Williamson <awilliam@redhat.com> - 4.6-26.20190806git1c53390
- Tweak FedoraMessaging to publish 'image' in compose messages

* Thu Aug 01 2019 Adam Williamson <awilliam@redhat.com> - 4.6-25.20190806git1c53390
- Backport PR #2244 to fix some problems in load_templates

* Thu Aug 01 2019 Adam Williamson <awilliam@redhat.com> - 4.6-24.20190806git1c53390
- Bump to latest git again, drop all patches (all merged)

* Thu Aug 01 2019 Adam Williamson <awilliam@redhat.com> - 4.6-23.20190726git92e8f3c
- Prepend the topic_prefix to ci-messages messages also

* Thu Aug 01 2019 Adam Williamson <awilliam@redhat.com> - 4.6-22.20190726git92e8f3c
- Some fixes for the FedoraMessaging plugin

* Thu Aug 01 2019 Adam Williamson <awilliam@redhat.com> - 4.6-21.20190726git92e8f3c
- Allow AMQP messages with no prefix (backport PR #2236)

* Thu Aug 01 2019 Adam Williamson <awilliam@redhat.com> - 4.6-18.20190716git5bfa647.fc30.2
- Backport PR #2232 (faster and safer markdown rendering)
- Allow comments by users again (safe with PR #2232)

* Wed Jul 31 2019 Adam Williamson <awilliam@redhat.com> - 4.6-18.20190716git5bfa647.fc30.1
- Only allow operators and admins to post comments (security issue)

* Tue Jul 30 2019 Adam Williamson <awilliam@redhat.com> - 4.6-20.20190726git92e8f3c
- Add plugin for publishing fedora-messaging messages
- Backport PR #2232 (faster and safer markdown rendering)

* Fri Jul 26 2019 Adam Williamson <awilliam@redhat.com> - 4.6-19.20190726git92e8f3c
- Bump to latest git again
- Re-sync spec with upstream (including new python script subpackage)
- Drop merged patches

* Thu Jul 25 2019 Adam Williamson <awilliam@redhat.com> - 4.6-18.20190716git5bfa647
- Backport PR #2213 (fixes vulnerability to maliciously-formed API requests)
- Backport PR #2217 (allow passing headers to publish_amqp)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.6-17.20190716git5bfa647
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 16 2019 Adam Williamson <awilliam@redhat.com> - 4.6-16.20190716git5bfa647
- Update to latest git again, re-sync spec with upstream
- Enable AMQP plugin now the dependencies are packaged
- Backport some PRs to fix some test failures

* Mon Jun 03 2019 Adam Williamson <awilliam@redhat.com> - 4.6-15.20190603git8a35385
- Update to latest git again
- Fix update auto restart plugin for upstream changes

* Fri May 24 2019 Adam Williamson <awilliam@redhat.com> - 4.6-14.20190522gitab91f31
- Update to latest git again
- Drop merged patch

* Tue Mar 12 2019 Adam Williamson <awilliam@redhat.com> - 4.6-13.20190312gitb3e49dc
- Update to latest git again
- Revise the parallel cancel patch to match current PR state
- Drop merged patches

* Mon Mar 04 2019 Adam Williamson <awilliam@redhat.com> - 4.6-12.20190205git2b90641
- Backport fixes for various issues:
  + Parent and other child jobs being cancelled when a single child fails
  + Issue with download_asset task retry causing jobs to start prematurely
  + Retried minion tasks failing due to argument passing error

* Wed Feb 06 2019 Adam Williamson <awilliam@redhat.com> - 4.6-11.20190205git2b90641
- Bump to latest git again
- Drop merged patch
- Backport PR #1989 to avoid a minion parallel task issue
- Try dropping the 'restart on job died' patch to see current effects

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.6-10.20190114git5672fc3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Adam Williamson <awilliam@redhat.com> - 4.6-9.20190114git5672fc3
- Bump to latest git again with various bug fixes
- Drop merged patch

* Wed Jan 09 2019 Adam Williamson <awilliam@redhat.com> - 4.6-8.20190108git798c6f1
- Fix update restarter plugin for an upstream change

* Tue Jan 08 2019 Adam Williamson <awilliam@redhat.com> - 4.6-7.20190108git798c6f1
- Bump to latest git again, remove merged patch

* Tue Dec 18 2018 Adam Williamson <awilliam@redhat.com> - 4.6-6.20181218git66c0b50
- Bump to latest git again, remove backported patches
- Backport PR #1935 to fix another test failure due to IPC mocking

* Fri Nov 30 2018 Adam Williamson <awilliam@redhat.com> - 4.6-5.20181121gitb543647
- Backport PR #1901 to use Python 3 fedmsg-logger in fedmsg plugin

* Wed Nov 21 2018 Adam Williamson <awilliam@redhat.com> - 4.6-4.20181121gitb543647
- Bump to latest git again, now deps are available
- Update a couple of PR patches to latest versions
- Backport another PR to fix a test bug

* Tue Nov 20 2018 Adam Williamson <awilliam@redhat.com> - 4.6-3.20181113git3a06172
- Backport PR to fix UEFI var file handling with caching disabled

* Mon Nov 19 2018 Adam Williamson <awilliam@redhat.com> - 4.6-2.20181113git3a06172
- Backport a couple more useful changes
- Buildrequire glibc-langpack-en: see
  https://fedoraproject.org/wiki/Changes/Remove_glibc-langpacks-all_from_buildroot

* Wed Nov 14 2018 Adam Williamson <awilliam@redhat.com> - 4.6-1.20181113git3a06172
- Update to latest upstream git
  (Before PR#1783, we do not have the deps for that yet)
- Port changes from SUSE spec (new deps, UTF-8 makeinstall...)
- Make asset cache script more similar to SUSE's
- Backport a few PRs to fix test issues

* Mon Oct 01 2018 Adam Williamson <awilliam@redhat.com> - 4.5-13.20180207git3977d2f
- Adapt tests to logging changes in Mojolicious 8 (still works with 7)

* Fri Sep 28 2018 Adam Williamson <awilliam@redhat.com> - 4.5-12.20180207git3977d2f
- Restart workers on failure

* Thu Aug 23 2018 Adam Williamson <awilliam@redhat.com> - 4.5-11.20180207git3977d2f
- fedmsg plugin package requires daemonize

* Wed Aug 22 2018 Adam Williamson <awilliam@redhat.com> - 4.5-10.20180207git3977d2f
- Update fedmsg 'standard' patch to fix a few issues

* Tue Aug 21 2018 Adam Williamson <awilliam@redhat.com> - 4.5-9.20180207git3977d2f
- Emit individual openQA-internal job_create messages when posting an ISO
- Emit fedmsgs in new 'standard' format (as well as old format):
  https://pagure.io/fedora-ci/messages

* Fri Jul 20 2018 Adam Williamson <awilliam@redhat.com> - 4.5-8.20180207git3977d2f
- Backport a patch to handle a git error message case issue

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.5-7.20180207git3977d2f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Apr 20 2018 Adam Williamson <awilliam@redhat.com> - 4.5-6.20180207git3977d2f
- Don't auto-restart failed FreeIPA update tests
  They take forever and don't behave correctly on restart anyhow

* Fri Feb 09 2018 Adam Williamson <awilliam@redhat.com> - 4.5-5.20180207git3977d2f
- Bump to latest git again
- Fix tests to run with postgres

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.5-4.20171220gitbe13358
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Dec 21 2017 Adam Williamson <awilliam@redhat.com> - 4.5-3.20171220gitbe13358
- Bump AssetPack requirement

* Thu Dec 21 2017 Adam Williamson <awilliam@redhat.com> - 4.5-2.20171220gitbe13358
- Update to latest git again, drop merged patches
- Update spec with latest upstream changes (mainly to do with dropping sqlite)

* Thu Dec 21 2017 Adam Williamson <awilliam@redhat.com> - 4.4-66.20170908gitcc6c98a
- Update #1493 backport to final committed version (_ONLY_OBSOLETE_SAME_BUILD)

* Thu Nov 23 2017 Adam Williamson <awilliam@redhat.com> - 4.5-1.20171122git472b115
- Bump to near-latest git (versioned 4.5 upstream)
- Clean spec a bit, following upstream cleanup somewhat

* Wed Nov 08 2017 Adam Williamson <awilliam@redhat.com> - 4.4-65.20170908gitcc6c98a
- Backport _ONLYOBSOLETESAME scheduling parameter (PR #1493)

* Thu Sep 14 2017 Adam Williamson <awilliam@redhat.com> - 4.4-64.20170908gitcc6c98a
- Swap out my scheduler fix for the one mudler merged upstream

* Wed Sep 13 2017 Adam Williamson <awilliam@redhat.com> - 4.4-63.20170908gitcc6c98a
- Try to fix yet another scheduler issue (poo#25260)

* Mon Sep 11 2017 Adam Williamson <awilliam@redhat.com> - 4.4-62.20170908gitcc6c98a
- Bump to latest git again for attempted fix for poo#25124
- Patch from mudler to try and reduce websockets disconnections

* Fri Sep 08 2017 Adam Williamson <awilliam@redhat.com> - 4.4-61.20170908git257ef9f
- Bump to latest git yet again (one more scheduler fix)

* Thu Sep 07 2017 Adam Williamson <awilliam@redhat.com> - 4.4-60.20170905git1c421a8
- Bump to latest git (more scheduler fixes)
- Bump Mojolicious dep (new scheduler works poorly with 7.30)

* Thu Aug 17 2017 Adam Williamson <awilliam@redhat.com> - 4.4-59.20170817git9fa6353
- Bump to latest git
- Drop #1432 patch (now merged)

* Tue Aug 15 2017 Adam Williamson <awilliam@redhat.com> - 4.4-58.20170810git5b1e729
- Backport PR #1432 to hopefully improve remaining scheduler problems

* Thu Aug 10 2017 Adam Williamson <awilliam@redhat.com> - 4.4-57.20170810git5b1e729
- Bump to latest git again (more scheduler fixes)

* Fri Aug 04 2017 Adam Williamson <awilliam@redhat.com> - 4.4-56.20170804gitb5911e5
- Bump to latest git again (some tweaks to scheduling)
- Patch a new test to include . in INC

* Wed Aug 02 2017 Adam Williamson <awilliam@redhat.com> - 4.4-55.20170802git25c355a
- Drop notify_workers from update restart plugin

* Wed Aug 02 2017 Adam Williamson <awilliam@redhat.com> - 4.4-54.20170802git25c355a
- Bump to latest git again (with removal of job grabbing)

* Mon Jul 31 2017 Adam Williamson <awilliam@redhat.com> - 4.4-53.20170730git4c72a17
- Patch an issue in job grabbing that could cause workers to stall

* Thu Jul 27 2017 Adam Williamson <awilliam@redhat.com> - 4.4-52.20170730git4c72a17
- Update to latest git, drop merged patches
- Merge latest SUSE spec file changes

* Tue Jul 25 2017 Adam Williamson <awilliam@redhat.com> - 4.4-51.20170409gitfead7af
- Fix build (test suite) with Perl 5.26 (Rawhide)

* Tue Jul 25 2017 Adam Williamson <awilliam@redhat.com> - 4.4-50.20170409gitfead7af
- Recommend git (it's not required, but some features use it)

* Tue Apr 11 2017 Adam Williamson <awilliam@redhat.com> - 4.4-49.20170409gitfead7af
- Backport a couple of bugfix PRs (web UI flags, failed match border)

* Mon Apr 10 2017 Adam Williamson <awilliam@redhat.com> - 4.4-48.20170409gitfead7af
- Re-generate asset cache with AssetPack 1.41

* Mon Apr 10 2017 Adam Williamson <awilliam@redhat.com> - 4.4-47.20170409gitfead7af
- Update to latest git, drop all merged patches

* Wed Mar 29 2017 Adam Williamson <awilliam@redhat.com> - 4.4-46.20170130git8cc04a2
- Update the #1280 backport to final(?) version

* Wed Mar 29 2017 Adam Williamson <awilliam@redhat.com> - 4.4-45.20170130git8cc04a2
- Backport PR #1280 to fix 'tag' comment parsing for Fedora BUILDs

* Fri Mar 17 2017 Adam Williamson <awilliam@redhat.com> - 4.4-44.20170130git8cc04a2
- Update #1215 backport to fix some problems with it

* Tue Mar 14 2017 Adam Williamson <awilliam@redhat.com> - 4.4-43.20170130git8cc04a2
- Backport PR #1215 to prevent workers dying after failed API calls

* Wed Mar 01 2017 Adam Williamson <awilliam@redhat.com> - 4.4-42.20170130git8cc04a2
- Backport configurable build sort order feature from upstream master

* Wed Mar 01 2017 Adam Williamson <awilliam@redhat.com> - 4.4-41.20170130git8cc04a2
- Add a plugin that restarts Fedora update tests on failure

* Tue Feb 28 2017 Adam Williamson <awilliam@redhat.com> - 4.4-40.20170130git8cc04a2
- Fix a problem with the duplication patch that caused workers to be killed

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.4-39.20170130git8cc04a2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 30 2017 Adam Williamson <awilliam@redhat.com> - 4.4-38.20170130git8cc04a2
- Update to latest git, drop merged #1200 patch
- Split out client and doc packages (following SUSE)
- Add /usr/bin/openqa-client symlink (following SUSE)
- Update Mojolicious requirements
- Replace duplication patch with version that works against new code
- Backport #1211 to fix tests when Selenium is unavailable

* Wed Jan 25 2017 Adam Williamson <awilliam@redhat.com> - 4.4-37.20170104git3d6640e
- Backport PR #1200 to allow setting precedence order override

* Wed Jan 04 2017 Adam Williamson <awilliam@redhat.com> - 4.4-36.20170104git3d6640e
- Update to latest git, drop merged patch #1133

* Wed Jan 04 2017 Adam Williamson <awilliam@redhat.com> - 4.4-35.20170103git30ded4f
- Backport #1133 to improve the db deployment locking a bit

* Tue Jan 03 2017 Adam Williamson <awilliam@redhat.com> - 4.4-34.20170103git30ded4f
- Update to latest git again (many enhancements, inc. my DB schema upgrade one)
- Drop no-longer-needed dependency and merged patch

* Fri Dec 16 2016 Adam Williamson <awilliam@redhat.com> - 4.4-33.20161216git7addfed
- bump to latest git again, with brc/bgo patch merged
- backport PR #1087 to have initdb indicate result by exit code

* Wed Dec 14 2016 Adam Williamson <awilliam@redhat.com> - 4.4-32.20161213git2fb9bdb
- backport patch to add 'brc' (RHBZ) and 'bgo' (BGO) bug labels

* Tue Dec 13 2016 Adam Williamson <awilliam@redhat.com> - 4.4-31.20161213git2fb9bdb
- bump to latest git again (some useful-looking fixes)

* Mon Dec 05 2016 Adam Williamson <awilliam@redhat.com> - 4.4-30.20161205git84716b1
- bump to latest git again (get some upstream changes to fedmsg messages)
- Backport a PR to add comment ID to fedmsg comment messages
- BuildRequire Test::MockObject as AMQP test uses it

* Mon Nov 28 2016 Adam Williamson <awilliam@redhat.com> - 4.4-29.20161128git663c025
- Bump to latest git (general F25 cycle start bump, lots of new stuff)
- Port over spec changes from openSUSE

* Thu Nov 10 2016 Adam Williamson <awilliam@redhat.com> - 4.4-28.20161022git1f44aeb
- Backport patch to add 'before' and 'after' params to the API job query

* Mon Oct 24 2016 Adam Williamson <awilliam@redhat.com> - 4.4-27.20161022git1f44aeb
- backport #963 to fix worker handling of missing assets

* Sat Oct 22 2016 Adam Williamson <awilliam@redhat.com> - 4.4-26.20161022git1f44aeb
- bump to git one more time, all recent fixes merged upstream

* Fri Oct 21 2016 Adam Williamson <awilliam@redhat.com> - 4.4-25.20161020git877db25
- stop job cancellation breaking on artefact upload (and duplicating the job)

* Fri Oct 21 2016 Adam Williamson <awilliam@redhat.com> - 4.4-24.20161020git877db25
- latest git again (with #954 merged)
- latest version of #955
- backport #956 (fix group overview page for groups with no description)

* Thu Oct 20 2016 Adam Williamson <awilliam@redhat.com> - 4.4-23.20161020gitbaac24b
- latest git again (with #945), backport three asset fixups

* Wed Oct 19 2016 Adam Williamson <awilliam@redhat.com> - 4.4-22.20161019git91993f8
- latest git again, backport PR #945 (to fix asset cleanup)

* Thu Oct 06 2016 Adam Williamson <awilliam@redhat.com> - 4.4-21.20161006git1ad6190
- bump to latest git again, to get #920 (fix for asset download name)

* Fri Sep 23 2016 Adam Williamson <awilliam@redhat.com> - 4.4-20.20160922git23e4f45
- bump to latest git once more, coolo fixed more stuff

* Mon Sep 19 2016 Adam Williamson <awilliam@redhat.com> - 4.4-19.20160919git5c812db
- bump to latest git again, all patches merged except auto-dupe reversion

* Fri Sep 16 2016 Adam Williamson <awilliam@redhat.com> - 4.4-18.20160915git13b8eb4
- bump to latest git again (inc. garret's needle fix)
- update #883, rediff #875 on new #883, add an extra fix on top of #875

* Thu Sep 15 2016 Adam Williamson <awilliam@redhat.com> - 4.4-17.20160915git323d73a
- backport a couple of worker notification fixes I wrote

* Thu Sep 15 2016 Adam Williamson <awilliam@redhat.com> - 4.4-16.20160915git323d73a
- also backport garretraziel's needles-in-subdirs fix (#868)

* Thu Sep 15 2016 Adam Williamson <awilliam@redhat.com> - 4.4-15.20160915git323d73a
- bump to git master again, more fixes, backport #875

* Wed Sep 14 2016 Adam Williamson <awilliam@redhat.com> - 4.4-14.20160914git89e98b7
- bump to git master again, with better HMAC timestamp fix

* Mon Sep 12 2016 Adam Williamson <awilliam@redhat.com> - 4.4-13.20160912gitc185cf9
- bump to git master again, drop merged patches
- increase HMAC timestamp validity from 5 to 10 mins to workaround POO #13690

* Mon Sep 12 2016 Adam Williamson <awilliam@redhat.com> - 4.4-12.20160912git14305d0
- bump to latest git, drop merged patches
- drop my PR #844 patches in favour of coolo's #848 (merged upstream)
- backport PR #864 to make dead worker check less greedy

* Sat Sep 10 2016 Adam Williamson <awilliam@redhat.com> - 4.4-11.20160902gitee52128
- revert upstream's disabling of auto-duplication of 'unknown incomplete' jobs

* Sat Sep 03 2016 Adam Williamson <awilliam@redhat.com> - 4.4-10.20160902gitee52128
- bump to latest git (minor changes)

* Thu Sep 01 2016 Adam Williamson <awilliam@redhat.com> - 4.4-9.20160829git8609e09
- move the status_update timer removal back a bit
- latest tested upstream-submitted versions of PR #844 patches

* Wed Aug 31 2016 Adam Williamson <awilliam@redhat.com> - 4.4-8.20160829git8609e09
- ok, let's see if this works:
- keep the upload reversion (use non-blocking post)
- keep updating status till file upload completes
- checksum uploaded assets by 100MiB chunks to avoid long block on file read

* Wed Aug 31 2016 Adam Williamson <awilliam@redhat.com> - 4.4-7.20160829git8609e09
- re-apply the upload reversion so we use non-blocking post again...

* Wed Aug 31 2016 Adam Williamson <awilliam@redhat.com> - 4.4-6.20160829git8609e09
- worker: drop the inactivity time thing, didn't work

* Wed Aug 31 2016 Adam Williamson <awilliam@redhat.com> - 4.4-5.20160829git8609e09
- worker: keep updating status till file upload completes

* Wed Aug 31 2016 Adam Williamson <awilliam@redhat.com> - 4.4-4.20160829git8609e09
- try using simple blocking post for file upload with inactivity timeout

* Mon Aug 29 2016 Adam Williamson <awilliam@redhat.com> - 4.4-3.20160829git8609e09
- Complete revert of f2547e9 to see if it helps upload issues

* Mon Aug 29 2016 Adam Williamson <awilliam@redhat.com> - 4.4-2.20160829git8609e09
- update to latest git (should help with upload failures)
- apply PR #802 to see if it helps with job cancel failures

* Fri Aug 26 2016 Adam Williamson <awilliam@redhat.com> - 4.4-1.20160826git1ac2387
- update to latest git again
- SUSE switched to 4.4 as the base version, so follow that

* Fri Jul 08 2016 Adam Williamson <awilliam@redhat.com> - 4.3-30.20160708git84c9461
- update to latest git again
- drop merged patches: PR #767 and asset removal PR #773

* Wed Jul 06 2016 Adam Williamson <awilliam@redhat.com> - 4.3.29-20160706gitc34c90b
- Apply PR #767 to fix multiple interactive mode issues

* Wed Jul 06 2016 Adam Williamson <awilliam@redhat.com> - 4.3.28-20160706gitc34c90b
- bump to latest git again (fix fuzzy web UI logo)

* Tue Jul 05 2016 Adam Williamson <awilliam@redhat.com> - 4.3.27-20160630git1e9c29b
- bump to latest git again (some useful bug fixes landed)

* Mon Jun 27 2016 Adam Williamson <awilliam@redhat.com> - 4.3.26-20160627gita08377c
- bump to latest upstream git
- drop Assetpack-Bootstrap3 dep
- drop triggerin use and just pre-generate and package the asset cache
- add script for generating the asset cache (using a minimal mojo app)

* Tue May 24 2016 Adam Williamson <awilliam@redhat.com> - 4.3-25.20160413git45e4923
- backport support for configuring asset types not to show links for

* Wed Apr 13 2016 Adam Williamson <awilliam@redhat.com> - 4.3-24.20160413git45e4923
- bump a bit further to include garretraziel's HDD_1 search fix

* Thu Apr 07 2016 Adam Williamson <awilliam@redhat.com> - 4.3-23.20160408git968b05d
- rebase to current upstream git master (patch set is getting unwieldy)
- drop database migration scriptlets (done in openQA itself now)

* Thu Mar 31 2016 Adam Williamson <awilliam@redhat.com> - 4.3-22
- backport: allow needles to be in nested directories (jskladan)

* Thu Mar 10 2016 Adam Williamson <awilliam@redhat.com> - 4.3-21
- add a 'build' property to the fedmsg data

* Thu Mar 10 2016 Adam Williamson <awilliam@redhat.com> - 4.3-20
- let geekotest own share/factory instead of packaging factory/tmp
- backport PR that allows loading of config file-specified plugins
- add a plugin to emit fedmsgs

* Tue Mar 08 2016 Adam Williamson <awilliam@redhat.com> - 4.3-19
- package /var/lib/openqa/share/factory/tmp with appropriate ownership

* Mon Feb 29 2016 Adam Williamson <awilliam@redhat.com> - 4.3-18
- backports: make asset downloading more robust against unexpected cases

* Wed Feb 17 2016 Adam Williamson <awilliam@redhat.com> - 4.3-17
- backport: start services after database services
- backport: treat kernels/initrds as assets, allow download of all assets

* Wed Feb 17 2016 Adam Williamson <awilliam@redhat.com> - 4.3-16
- update the selenium-skipping patch to a better version

* Tue Feb 16 2016 Adam Williamson <awilliam@redhat.com> - 4.3-15
- fix mode of generate-packed-assets (stupid RPM...)
- backport patch to not install unneeded scripts
- don't do prove -r twice in check

* Tue Feb 16 2016 Adam Williamson <awilliam@redhat.com> - 4.3-14
- re-organize requires in spec file
- fix the tests to run if perl(Selenium) bits aren't available
- backport fix for worker systemd unit with newer systemd
- enable test suite (some tests are skipped, but better than nothing)

* Tue Feb 16 2016 Adam Williamson <awilliam@redhat.com> - 4.3-13
- update backported patches that have been merged upstream now
- backport generate-packed-assets instead of adding it as SOURCE1

* Fri Feb 12 2016 Adam Williamson <awilliam@redhat.com> - 4.3-12
- quiet the trigger script down a bit
- clean up sass cache in the trigger script
- more customizable trigger script for upstream submission
- setgid in upgradedb as well as initdb

* Fri Feb 12 2016 Adam Williamson <awilliam@redhat.com> - 4.3-11
- fix initdb UID / GID issues
- use triggers for packed asset (re-)generation (Zbigniew)
- server should own script dir as well as worker
- drop ownership / ghosting of specific asset dirs

* Wed Feb 10 2016 Adam Williamson <awilliam@redhat.com> - 4.3-10
- log to journal by default (upstream PR #541)

* Mon Feb 08 2016 Adam Williamson <awilliam@redhat.com> - 4.3-9
- drop the log file ghost stuff, it's for AppArmor, not needed for Fedora
- comment on the requirement for remote workers to mount shared data
- explain the location of the compat symlinks in -common
- fix ownership of database.ini (thanks Zbigniew)

* Sun Feb 07 2016 Adam Williamson <awilliam@redhat.com> - 4.3-8
- more package review improvements:
- * drop the old commented perl(EV) conflict which isn't needed now
- * don't use systemd_requires macro
- * explain that build is a lie (but make it parallel nothing)
- * move check to the logical place
- * don't fail scriptlets on user creation failure
- * move post-install info message to httpd subpackage
- * openqa.ini does not need to be owned by geekotest
- * don't own directories we shouldn't

* Fri Feb 05 2016 Adam Williamson <awilliam@redhat.com> - 4.3-7
- package review improvements:
- * no need for worker to Requires(post) os-autoinst
- * explain why tests are currently disabled
- * fix a few macro invocations to use curly braces
- * use directory macros where appropriate in scriptlets
- * split apache configuration into a subpackage

* Thu Jan 28 2016 Adam Williamson <awilliam@redhat.com> - 4.3-6
- update ISOURL patch to latest revision

* Thu Jan 28 2016 Adam Williamson <awilliam@redhat.com> - 4.3-5
- patch: fix ISO downloading when ISOURL is specified but not ISO

* Wed Jan 27 2016 Adam Williamson <awilliam@redhat.com> - 4.3-4
- patch: stop gru task barfing on malformed JSON (upstream PR #518)

* Fri Jan 15 2016 Adam Williamson <awilliam@redhat.com> - 4.3-3
- filter perl(Perl::Critic) auto-requires, only needed for tests

* Fri Jan 15 2016 Adam Williamson <awilliam@redhat.com> - 4.3-2
- fix __requires_exclude (stray | made it too greedy)

* Fri Jan 15 2016 Adam Williamson <awilliam@redhat.com> - 4.3-1
- new release 4.3, drop patches merged upstream
- tweak auto-provides / requires filtering
- backport fix for slowdown caused by using dbus for thumbnails
- update database on package update
- include license in -common

* Tue Jan 05 2016 Adam Williamson <awilliam@redhat.com> - 4.2-12
- one more backport (of a PR I just wrote) for HDD cleanup

* Mon Jan 04 2016 Adam Williamson <awilliam@redhat.com> - 4.2-11
- backport cleanup of generated HDD snapshots

* Wed Dec 16 2015 Adam Williamson <awilliam@redhat.com> - 4.2-10
- backport tmpdir creation fix (prevents large uploads failing)

* Wed Dec 02 2015 Adam Williamson <awilliam@redhat.com> - 4.2-9
- backport branding fix (removes SUSE navbar)

* Tue Nov 17 2015 Adam Williamson <awilliam@redhat.com> - 4.2-8
- make create_admin executable

* Sat Oct 24 2015 Adam Williamson <awilliam@redhat.com> - 4.2-7
- conflict with perl(EV) - see openQA GH #450

* Thu Oct 22 2015 Adam Williamson <awilliam@redhat.com> - 4.2-6
- backport sqlite security fix and admin user creation script

* Sat Oct 17 2015 Adam Williamson <awilliam@redhat.com> - 4.2-5
- correct worker username in a couple of places, adjust perms

* Sat Oct 17 2015 Adam Williamson <awilliam@redhat.com> - 4.2-4
- another dep fix: sqlite

* Sat Oct 17 2015 Adam Williamson <awilliam@redhat.com> - 4.2-3
- correct some dependencies, exclude internal auto-generated reqs

* Fri Oct 16 2015 Adam Williamson <awilliam@redhat.com> - 4.2-2
- fix apache config filenames in sed commands

* Thu Oct 15 2015 Adam Williamson <awilliam@redhat.com> - 4.2-1
- update to 4.2 upstream, tweak spec a bit more

* Fri Aug 14 2015 Adam Williamson <awilliam@redhat.com> - 4-1.20150814gitc66ff87
- initial package (based on openSUSE spec)
