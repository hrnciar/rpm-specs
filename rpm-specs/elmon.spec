# Review Request: https://bugzilla.redhat.com/show_bug.cgi?id=1197517

Name:           elmon
Version:        13b1
Release:        11%{?dist}
Summary:        Performance monitoring tool

License:        GPLv3
URL:            http://elmon.sourceforge.net/
Source0:        http://sourceforge.net/projects/%{name}/files/%{name}_%{version}.tar

BuildRequires:  gcc
BuildRequires:  ncurses-devel

%description
elmon is a performance monitoring tool for Linux. It provides an ncurses
interface as well as the ability to save the data to a CSV file. elmon is based
on nmon by Nigel Griffiths and the CSV output is compatible with nmon processing
tools.

elmon provides performance information on CPU, memory, network, disk, file
system usage, etc.

If you are familiar with nmon, here are the additional features that elmon
supports:
o Multi-column output.
o Interactive Help Menu
o Stat sections are displayed in the order that the user enables them
o Long term CPU graph will use up the entire width of the screen
o Supports subsecond screen refreshes
o New Memory/Swap graph
o Multiple bug fixes (including several bug fixes supplied by David Baril on
nmon forum).


%prep
%setup -q -c %{name}-%{version}


%build
%{make_build} elmon_x86_rhel52


%install
mkdir -p %{buildroot}/%{_bindir}
install elmon_x86_rhel52 %{buildroot}/%{_bindir}/%{name}

%files
%doc change_log.txt
%license license.txt
%{_bindir}/%{name}


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 13b1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 13b1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 13b1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 13b1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 13b1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 13b1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 13b1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 13b1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Oct 26 2016 Pavel Alexeev <Pahan@Hubbitus.info> - 13b1-3
- Drop BR gcc

* Tue Sep 13 2016 Pavel Alexeev <Pahan@Hubbitus.info> - 13b1-2
- Shorter description.
- Cleanup.
- Add BR gcc
- Use make_build macros.

* Sun Mar  1 2015 Pavel Alexeev (aka Pahan-Hubbitus) <Pahan@Hubbitus.info> - 13b1-1
- Initial spec
