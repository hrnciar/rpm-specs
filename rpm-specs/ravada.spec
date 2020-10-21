Name:           ravada
Version:        0.8.3
Release:        3%{?dist}
Summary:        Remote Virtual Desktops Manager
# AGPLv3: main program
# ASL 2.0: public/css/sb-admin.css
#          public/js/main.js
License:        AGPLv3 and ASL 2.0
URL:            https://ravada.upc.edu/
Source0:        https://github.com/UPC/ravada/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
%{?systemd_requires}
BuildRequires:  systemd
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Authen::Passphrase)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Date::Calc)
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(DBIx::Connector)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(feature)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Rsync)
BuildRequires:  perl(Hash::Util)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(Image::Magick)
BuildRequires:  perl(I18N::LangTags::Detect)
BuildRequires:  perl(IO::Interface)
BuildRequires:  perl(IPC::Run3)
BuildRequires:  perl(IPTables::ChainMgr)
BuildRequires:  perl(JSON::XS)
BuildRequires:  perl(lib)
BuildRequires:  perl(Locale::Maketext::Lexicon)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Mojolicious) >= 6.15
BuildRequires:  perl(Mojolicious::Plugin::I18N)
BuildRequires:  perl(Mojolicious::Plugin::RenderFile)
BuildRequires:  perl(Moose)
BuildRequires:  perl(MooseX::Types::NetAddr::IP)
BuildRequires:  perl(Net::DNS)
BuildRequires:  perl(Net::LDAP)
BuildRequires:  perl(Net::Ping)
BuildRequires:  perl(Net::SSH2)
BuildRequires:  perl(Parallel::ForkManager)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(strict)
BuildRequires:  perl(Sys::Statistics::Linux)
BuildRequires:  perl(Sys::Virt)
BuildRequires:  perl(Test::Moose::More)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Test::Perl::Critic)
BuildRequires:  perl(Test::SQL::Data)
BuildRequires:  perl(Time::Piece)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XML::LibXML)
BuildRequires:  perl(YAML)
# For tests
BuildRequires:  iptables
BuildRequires:  ImageMagick
BuildRequires:  libvirt
BuildRequires:  mariadb-common
BuildRequires:  qemu-img
BuildRequires:  wget
Requires:       perl(Mojolicious::Plugin::I18N)
Requires:       perl(Mojolicious::Plugin::RenderFile)
Requires:       iptables
Requires:       libvirt
Requires:       mariadb-common
Requires:       qemu-img
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires(pre):  shadow-utils
Recommends:     virt-viewer

%description
Ravada is a software that allows the user to connect to a remote virtual
desktop.

In the current release we use the KVM Hypervisors: KVM as the backend for the
Virtual Machines. LXC support is currently in development.

%prep
%autosetup -p1 -n %{name}-%{version}

# Fedora doesn't ship kvm-spice but qemu-kvm
find . -type f -name "*.xml" -exec sed -i 's|kvm-spice|qemu-kvm|g' {} ';'

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="$RPM_OPT_FLAGS"
%make_build

%install
%make_install
%{_fixperms} %{buildroot}/*

install -Dpm 0755 script/rvd_front %{buildroot}%{_sbindir}/rvd_front
install -Dpm 0755 script/rvd_back  %{buildroot}%{_sbindir}/rvd_back
install -Dpm 0644 etc/ravada.conf %{buildroot}%{_sysconfdir}/ravada.conf
install -Dpm 0644 etc/rvd_front.conf.example %{buildroot}%{_sysconfdir}/rvd_front.conf
install -Dpm 0644 etc/systemd/rvd_back.service %{buildroot}%{_unitdir}/rvd_back.service
install -Dpm 0644 etc/systemd/rvd_front.service %{buildroot}%{_unitdir}/rvd_front.service
mkdir -p %{buildroot}%{_localstatedir}/lib/%{name}
cp -aR etc/xml %{buildroot}%{_localstatedir}/lib/%{name}/
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -aR public %{buildroot}%{_datadir}/%{name}/
cp -aR templates %{buildroot}%{_datadir}/%{name}/

# Remove empty files
find %{buildroot} -size 0 -delete

%check
# silently ignore errors
make test || :

%pre
getent group ravada >/dev/null || groupadd -r ravada
getent passwd ravada >/dev/null || \
    useradd -r -g ravada -d %{_localstatedir}/lib/ravada -s /sbin/nologin \
    -c "Ravada user account" ravada
exit 0

%post
%systemd_post rvd_back.service
%systemd_post rvd_front.service

%preun
%systemd_preun rvd_back.service
%systemd_preun rvd_front.service

%postun
%systemd_postun_with_restart rvd_back.service
%systemd_postun_with_restart rvd_front.service

%files
%doc CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md README.md sql
%license LICENSE
%{_sbindir}/rvd_back
%{_sbindir}/rvd_front
%{perl_vendorlib}/*
%config(noreplace) %{_sysconfdir}/*.conf
%{_datadir}/%{name}/
%{_localstatedir}/lib/%{name}/
%{_mandir}/man3/*
%{_unitdir}/*.service


%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 01 17:04:59 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.8.3-1
- Update to 0.8.3 (#18525875)

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.8.2-2
- Perl 5.32 rebuild

* Thu Jun 18 15:48:06 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.8.2-1
- Update to 0.8.2

* Sat Feb 22 00:52:38 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.6.0-1
- Update to 0.6.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 17 17:18:48 CET 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.5.0-1
- Release 0.5.0 (#1784421)

* Thu Aug 08 22:23:27 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.4.8-1
- Release 0.4.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 16 18:39:51 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.4.5-1
- Release 0.4.5

* Mon Jun 10 18:15:19 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.4.3-1
- Release 0.4.3 (#1716693)

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.4.1-2
- Perl 5.30 rebuild

* Thu May 30 15:33:02 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.4.1-1
- Release 0.4.1 (#1715450)

* Mon May 27 22:16:13 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.4.0-1
- Release 0.4.0 (#1714171)

* Fri Apr 12 16:43:04 CET 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.3.5-1
- Release 0.3.5 (#1699383)

* Thu Mar 14 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.3.4-1
- Release 0.3.4

* Tue Feb 19 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.3.3-1
- Release 0.3.3

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 15 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.3.2-1
- Release 0.3.2

* Wed Oct 24 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.3.1-1
- Release 0.3.1

* Thu Oct 18 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.3.0-1
- Release 0.3.0

* Wed Aug 01 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.3.0-0.2.beta6
- Add missing BR for tests
- Install rvd_benchmark_create

* Fri Jul 27 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.3.0-0.1.beta6
- Pre-release 0.3.0 beta6

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.2.17-2
- Perl 5.28 rebuild

* Tue Jun 05 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.2.17-1
- Release 0.2.17

* Fri Jun 01 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.2.16-1
- Release 0.2.16

* Thu May 10 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.2.15-1
- Release 0.2.15

* Mon Mar 19 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.2.14-1
- Release 0.2.14

* Wed Feb 28 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.2.13-2
- Fix incorrect kvm binary

* Wed Feb 28 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.2.13-1
- Release 0.2.13
- Fix rvd_back/rvd_front installation

* Tue Feb  6 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.2.13-0.1.20180117gitf70dfbf
- Pre-release 0.2.13

* Tue Jan 16 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.2.12-1
- Upstream release 0.2.12

* Mon Dec 04 2017 Robert-André Mauchin <zebob.m@gmail.com> - 0.2.10-1
- Specfile autogenerated by cpanspec 1.78.
