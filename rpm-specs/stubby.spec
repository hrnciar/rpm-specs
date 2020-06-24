%global git_commit 7939e9652acb120d43d37db2eb0dea986f29785b
%global git_date 20200318

%global git_short_commit %(echo %{git_commit} | cut -c -8)
%global git_suffix %{git_date}git%{git_short_commit}


Name:           stubby
Version:        0.3.1
Release:        0.2.%{git_suffix}%{?dist}
Summary:        Application that act as a local DNS Privacy stub resolver

License:        BSD
URL:            https://github.com/getdnsapi/%{name}
Source0:        https://github.com/getdnsapi/stubby/archive/%{git_commit}/%{name}-%{version}.tar.gz

Provides:       getdns-stubby = 1.6.0-2
Obsoletes:      getdns-stubby < 1.6.0-2

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  cmake
BuildRequires:  getdns-devel
BuildRequires:  libyaml-devel
BuildRequires:  systemd-rpm-macros

Patch1:         stubby-0.3.1-dnssec-ta.patch


%description
Stubby is a local DNS Privacy stub resolver (using DNS-over-TLS).
Stubby encrypts DNS queries sent from a client machine to a 
DNS Privacy resolver increasing end user privacy.


%prep
%autosetup -n stubby-%{git_commit}


%build
%cmake -DCMAKE_BUILD_TYPE:STRING=Release .
%make_build


%install
%make_install
find %{buildroot} -size 0 -delete
mkdir -p %{buildroot}%{_unitdir}
install -pm 0644 systemd/stubby.service %{buildroot}%{_unitdir}/stubby.service


%files
%{_bindir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}
%{_unitdir}/stubby.service
%{_mandir}/man1/%{name}.1.gz
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/AUTHORS
%license %{_docdir}/%{name}/COPYING
%{_docdir}/%{name}/ChangeLog
%{_docdir}/%{name}/README.md


%changelog
* Wed Mar 18 2020 Artem Egorenkov <aegorenk@redhat.com> - 0.3.1-0.2.20200318git7939e965
- Snapshot information field added
- systemd-rpm-macros added to build requirements
- systemd-devel and systemd removed from build requirements
- Obsoletes version for getns-stubby fixed

* Thu Mar 12 2020 Artem Egorenkov <aegorenk@redhat.com> - 0.3.1-0.1.29785b
- First stubby package
