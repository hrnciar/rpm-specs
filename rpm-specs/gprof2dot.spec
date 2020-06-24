%global         usegit      1
%global         mainrel     0.18

%global         githash     6dc9bdf4b01627aba20f8f581fea2c429f5e5927
%global         shorthash   %(TMP=%githash ; echo ${TMP:0:10})
%global         gitdate     Mon, 26 Aug 2019 11:00:30 +0200
%global         gitdate_num 20190826

%if 0%{?usegit} >= 1
%global         fedorarel   %{mainrel}.D%{gitdate_num}git%{shorthash}
%else
%global         fedorarel   %{?prever:0.}%{mainrel}%{?prever:.%{prerpmver}}
%endif

%global	description_common \
This is a Python script to convert the output from prof, gprof, oprofile,\
Shark, AQtime, and python profilers into a dot graph.  It has the following\
features:\
\
* can correctly parse C++ template function names\
* allows to prune nodes and edges below a certain threshold\
* uses an heuristic to propagate time inside mutually recursive functions\
* uses color efficiently to draw attention to hot-spots\
%{nil}


Name:           gprof2dot
Version:        1.0
Release:        %{fedorarel}%{?dist}.2
Summary:        Generate dot graphs from the output of several profilers

License:        LGPLv3+
URL:            https://github.com/jrfonseca/gprof2dot
Source0:        https://github.com/jrfonseca/gprof2dot/archive/%{githash}/%{name}-%{version}-D%{gitdate_num}git%{githash}.tar.gz
BuildArch: noarch

Obsoletes:      python2-%{name} < 1.0-0.17
Obsoletes:      python3-%{name} < 1.0-0.17
Obsoletes:      %{name}-python3 < 1.0-0.17
BuildRequires:  python3
BuildRequires:  graphviz

%global _description\
%description_common

%description %_description

%prep
%setup -q -n %{name}-%{githash}

%build
%if 0%{?fedora} < 31
exit 1
%endif

%install
mkdir -p %{buildroot}%{_bindir}

install -p -m 0755 gprof2dot.py %{buildroot}%{_bindir}/gprof2dot
sed -i %{buildroot}%{_bindir}/gprof2dot \
	-e 's|/usr/bin/env[ \t][ \t]*python$|%{_bindir}/python3|'

%check
python3 ./tests/test.py

%files
%license LICENSE.txt
%doc README.md
%doc sample.png
%doc schema.json

%{_bindir}/gprof2dot

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.18.D20190826git6dc9bdf4b0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct  1 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0-0.18.100.D20190826git6dc9bdf4b0
- Fix Obsoletes

* Tue Oct  1 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0-0.17.100.D20190826git6dc9bdf4b0
- Update to the latest git
- F-31+: ship python3 only, obsolete all subpackages

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.16.D20160727git78310e7637.8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.16.D20160727git78310e7637.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.16.D20160727git78310e7637.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.16.D20160727git78310e7637.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.0-0.16.D20160727git78310e7637.4
- Python 2 binary package renamed to python2-gprof2dot
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.16.D20160727git78310e7637.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.16.D20160727git78310e7637.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.0-0.16.D20160727git78310e7637.1
- Rebuild for Python 3.6

* Thu Aug 18 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0-0.16.D20160727git78310e7637
- New upstream snapshot
- Create python3 subpackage

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.15.20150131gitc1354af
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.14.20150131gitc1354af
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Mar  4 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0-0.13.20150131gitc1354af
- New upstream snapshot (actually same as pypi 2015.02.03)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.12.20130226git1ef99
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.11.20130226git1ef99
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Feb 26 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 1.0-0.9.20130226git1ef99
- New upstream snapshot

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.9.20120720git56961
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Toshio Kuratomi <toshio@fedoraproject.org> - 1.0-0.8.20120720git56961
- Update to solve https://bugzilla.redhat.com/show_bug.cgi?id=821864 (support perf)
- Upstream has switched to a git repo

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.7.20100708hg89
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.6.20100708hg89
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.5.20100708hg89
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 08 2010 Toshio Kuratomi <toshio@fedoraproject.org> - 1.0-0.4.20100708hg89
- Update to new upstream

* Tue Apr 13 2010 Toshio Kuratomi <toshio@fedoraproject.org> - 1.0-0.3.20100413hg88
- Update to new upstream

* Mon Sep 14 2009 Toshio Kuratomi <toshio@fedoraproject.org> - 1.0-0.2.20090901svn
- Use svn export instead of svn checkout to generate the tarball
- Replace use of env with direct call to the python interpreter

* Tue Sep 1 2009 Toshio Kuratomi <toshio@fedoraproject.org> - 1.0-0.1.20090901svn
- Initial Fedora build
