# vim: syntax=spec
%global gitcommit 2ad8f164de98f305cf52fa0539876ac500fa3bba
%global gitshortcommit %(c=%{gitcommit}; echo ${c:0:7})
%global snapshotdate 20200520

Name:           memstrack
Version:        0.1.5
Release:        1%{?dist}
Summary:        A memory allocation tracer, like a hot spot analyzer for memory allocation
License:        GPLv3
URL:            https://github.com/ryncsn/memstrack
VCS:            git+git@github.com:ryncsn/memstrack.git
BuildRequires:  gcc
BuildRequires:  ncurses-devel

Source:         https://github.com/ryncsn/memstrack/archive/%{gitcommit}/memstrack-%{gitshortcommit}.tar.gz

%description
A memory allocation tracer, like a hot spot analyzer for memory allocation

%prep
%setup -q -n memstrack-%{gitcommit}

%build
%{set_build_flags}
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}/%{_bindir}
install -p -m 755 memstrack %{buildroot}/%{_bindir}

%files
%doc README.md
%license LICENSE
%{_bindir}/memstrack

%changelog
* Sat May 30 2020 Kairui Song <ryncsn@gmail.com> - 0.1.5-1
- Update to upstream latest release

* Tue Apr 21 2020 Kairui Song <ryncsn@gmail.com> - 0.1.2-1
- Update to upstream latest release

* Sun Mar 15 2020 Kairui Song <ryncsn@gmail.com> - 0-1.20200310gitee02de2
- First release
