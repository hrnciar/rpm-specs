# Upstream has only made one release, but there have been lots of bug fixes
# since, so we use a git checkout.
%global commit      a258e78f17abdf2ce21c2515cfe8306a44774e2a
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global gitdate     20200729

# The subpackage layout was designed with the following points in mind:
# 1. The scripts are very small, so packing them together doesn't hurt much.
#    On the other hand, doing a fine-grained separation into subpackages
#    results in the metadata taking up a huge percentage of the packages.
# 2. The demo graphs are large, on the other hand, and few people will want to
#    see them, so they get their own package.
# 3. Most users only want flamegraph.pl, so it gets its own package.
# 4. The perf scripts have an external dependency on binutils, and the php
#    script has an external dependency on php, so they get their own packages.
# 5. All the rest are lumped together, due to the considerations in #1.  They
#    have varying licenses and purposes, it is true, but we lump them together
#    anyway for space efficiency reasons.

Name:           flamegraph
Version:        1.0
Release:        6.%{gitdate}.%{shortcommit}%{?dist}
Summary:        Stack trace visualizer

License:        CDDL-1.0
URL:            http://www.brendangregg.com/flamegraphs.html
Source0:        https://github.com/brendangregg/FlameGraph/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
BuildArch:      noarch

BuildRequires:  help2man
BuildRequires:  perl-generators
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(open)
BuildRequires:  php-cli

%description
Flame graphs visualize profiled code.  Stack samples can be captured
using Linux perf_events, FreeBSD pmcstat (hwpmc), DTrace, SystemTap, and
many other profilers.  This package contains only the visualizer script,
flamegraph.pl.

%package        demos
Summary:        Demos of graphs produced by flamegraph

%description    demos
Demonstration graphs produced by flamegraph.

%package        stackcollapse
Summary:        Stack collapsers and support scripts
# The project as a whole is CDDL-1.0.  Exceptions to this license are:
# ASL 2.0: files.pl
# BSD: stackcollapse-pmc.pl, stackcollapse-sample.awk
# GPLv2+: difffolded.pl, stackcollapse-bpftrace.pl, stackcollapse-go.pl,
#     stackcollapse-jstack.pl
License:        CDDL-1.0 and ASL 2.0 and BSD and GPLv2+
Requires:       %{name} = %{version}-%{release}

%description    stackcollapse
A set of scripts that collapse stack traces produced by various tools
for consumption by flamegraph, as well as some miscellaneous support
scripts.

%package        stackcollapse-perf
Summary:        Stack collapser for perf output
# pkgsplit-perf.pl and range-perf.pl are ASL 2.0.
# The rest are CDDL-1.0.
License:        CDDL-1.0 and ASL 2.0
Requires:       %{name} = %{version}-%{release}
Requires:       binutils

%description    stackcollapse-perf
Scripts for collapsing perf output for consumption by flamegraph.

%package        stackcollapse-php
Summary:        Stack collapser for PHP
License:        GPLv2+
Requires:       %{name} = %{version}-%{release}

%description    stackcollapse-php
A script for collapsing PHP trace output for consumption by flamegraph.

%prep
%autosetup -n FlameGraph-%{commit}

fixtimestamp() {
  touch -r $1.orig $1
  rm -f $1.orig
}

# Do not use env
sed -i.orig 's,bin/env ,bin/,' stackcollapse-pmc.pl
fixtimestamp stackcollapse-pmc.pl

# Fix end of line encodings
sed -i.orig 's/\r//' stackcollapse-vtune.pl
fixtimestamp stackcollapse-vtune.pl

# Add a missing executable bit
chmod a+x stackcollapse-vtune.pl

%build
# Build man pages.  Some scripts produce no useful output with --help.
HELP2MANFLAGS="-N --version-string=%{version} --no-discard-stderr"
for fil in aix-perf.pl difffolded.pl files.pl flamegraph.pl range-perf.pl \
           stackcollapse-elfutils.pl stackcollapse-go.pl \
           stackcollapse-java-exceptions.pl stackcollapse-jstack.pl \
           stackcollapse-perf.pl stackcollapse-xdebug.php; do
  help2man $HELP2MANFLAGS ./$fil > $fil.1
done

%install
# Install the scripts
mkdir -p %{buildroot}%{_bindir}
cp -p *.{awk,php,pl} jmaps %{buildroot}%{_bindir}

# Install the man pages
mkdir -p %{buildroot}%{_mandir}/man1
cp -p *.1 %{buildroot}%{_mandir}/man1

%check
./test.sh

%files
%doc README.md
%license docs/cddl1.txt
%{_bindir}/flamegraph.pl
%{_mandir}/man1/flamegraph.pl.1*

%files          demos
%doc demos/*

%files          stackcollapse
%{_bindir}/difffolded.pl
%{_bindir}/files.pl
%{_bindir}/jmaps
%{_bindir}/stackcollapse.pl
%{_bindir}/stackcollapse-aix.pl
%{_bindir}/stackcollapse-bpftrace.pl
%{_bindir}/stackcollapse-elfutils.pl
%{_bindir}/stackcollapse-gdb.pl
%{_bindir}/stackcollapse-go.pl
%{_bindir}/stackcollapse-instruments.pl
%{_bindir}/stackcollapse-java-exceptions.pl
%{_bindir}/stackcollapse-jstack.pl
%{_bindir}/stackcollapse-ljp.awk
%{_bindir}/stackcollapse-pmc.pl
%{_bindir}/stackcollapse-recursive.pl
%{_bindir}/stackcollapse-sample.awk
%{_bindir}/stackcollapse-stap.pl
%{_bindir}/stackcollapse-vsprof.pl
%{_bindir}/stackcollapse-vtune.pl
%{_mandir}/man1/difffolded.pl.1*
%{_mandir}/man1/files.pl.1*
%{_mandir}/man1/stackcollapse-elfutils.pl.1*
%{_mandir}/man1/stackcollapse-go.pl.1*
%{_mandir}/man1/stackcollapse-java-exceptions.pl.1*
%{_mandir}/man1/stackcollapse-jstack.pl.1*
%{_mandir}/man1/stackcollapse-perf.pl.1*

%files          stackcollapse-perf
%{_bindir}/aix-perf.pl
%{_bindir}/pkgsplit-perf.pl
%{_bindir}/range-perf.pl
%{_bindir}/stackcollapse-perf.pl
%{_bindir}/stackcollapse-perf-sched.awk
%{_mandir}/man1/aix-perf.pl.1*
%{_mandir}/man1/range-perf.pl.1*
%{_mandir}/man1/stackcollapse-perf.pl.1*

%files          stackcollapse-php
%{_bindir}/stackcollapse-xdebug.php
%{_mandir}/man1/stackcollapse-xdebug.php.1*

%changelog
* Tue Aug 11 2020 Jerry James <loganjerry@gmail.com> - 1.0-6.20200729.a258e78
- Update to latest git HEAD for JVM fix

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-5.20191024.1a0dc69
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-4.20191024.1a0dc69
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov  4 2019 Jerry James <loganjerry@gmail.com> - 1.0-3.20191024.1a0dc69
- Update to latest git HEAD for bug fixes
- Add man pages

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-2.20190216.1b1c6de
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun  3 2019 Jerry James <loganjerry@gmail.com> - 1.0-1.20190216.1b1c6de
- Initial package
