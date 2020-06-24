Name:		topline
Version:	0.3
Release:	1%{?dist}
Summary:	Per-core/NUMA CPU and disk utilization plain-text grapher
License:	GPLv2+
URL:		https://github.com/kilobyte/topline
Source0:	https://github.com/kilobyte/topline/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:	make
BuildRequires:	gcc

%description
This is a top-of-the-line logger of CPU usage patterns, designed for
machines with ca. 50-300 total hardware threads (fewer works but results
in a narrow graph, more requires a very wide terminal).  Every per-tick
sample is shown abusing Unicode characters to fit within a single line.

Disk usage is also shown in a similarly terse per-device way, as %%
utilization for reads and writes.

%prep
%setup -q

%build
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_bindir} %{buildroot}%{_mandir}/man1
install topline %{buildroot}%{_bindir}
cp -p topline.1* %{buildroot}%{_mandir}/man1

%files
%{_bindir}/topline
%{_mandir}/man1/topline.1*
%license LICENSE
%doc README.md

%changelog
* Tue Feb 25 2020 Adam Borowski <kilobyte@angband.pl> 0.3-1
- Latest upstream.
- Review issues (capitalize short desc, license name, man page perms).

* Mon Jan 27 2020 Adam Borowski <kilobyte@angband.pl> 0.2-1
- Initial packaging.
