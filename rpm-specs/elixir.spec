%global debug_package %{nil}
%global __with_rebar 1
# We don't use rebar3 for now
%global __with_rebar3 0

Name:           elixir
Version:        1.10.2
Release:        3%{?dist}
Summary:        A modern approach to programming for the Erlang VM

License:        ASL 2.0
URL:            http://elixir-lang.org/

Source0:        https://github.com/elixir-lang/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        https://github.com/elixir-lang/%{name}/releases/download/v%{version}/Docs.zip#/%{name}-%{version}-doc.zip
# See https://bugzilla.redhat.com/1470583
#BuildArch:      noarch
BuildRequires: erlang-compiler
BuildRequires: erlang-crypto
BuildRequires: erlang-dialyzer
BuildRequires: erlang-erts
BuildRequires: erlang-eunit
BuildRequires: erlang-inets
BuildRequires: erlang-kernel
BuildRequires: erlang-parsetools
BuildRequires: erlang-public_key
%if %{__with_rebar}
BuildRequires: erlang-rebar
%endif %{__with_rebar}
%if %{__with_rebar3}
BuildRequires: erlang-rebar3
%endif %{__with_rebar3}
BuildRequires: erlang-sasl
BuildRequires: erlang-stdlib
BuildRequires: erlang-tools
BuildRequires: erlang-xmerl
BuildRequires: git
BuildRequires: sed
Requires: erlang-compiler
Requires: erlang-crypto
Requires: erlang-erts
#Requires: erlang-eunit
Requires: erlang-inets
Requires: erlang-kernel
Requires: erlang-parsetools
Requires: erlang-public_key
Requires: erlang-sasl
Requires: erlang-stdlib
Requires: erlang-tools


%description
Elixir is a programming language built on top of the Erlang VM.
As Erlang, it is a functional language built to support distributed,
fault-tolerant, non-stop applications with hot code swapping.

%prep
# Unpack the HTML documentation (Source1)
%setup -q -T -c -n %{name}-%{version}/docs -a 1
find -name ".build" -exec rm \{\} \;

# Unpack elixir itself (Source0)
%setup -q -D

# Remove windows-specific scripts
find -name '*.bat' -exec rm \{\} \;

# This contains a failing test. We want `make test` for most tests, but
# this deals with ANSI codes which rpmbuild strips.
rm lib/elixir/test/elixir/io/ansi_test.exs

# Remove VCS-specific files
find . -name .gitignore -delete
find . -name .gitkeep -delete

# Let the Makefile speak!
sed -i '/^Q\s*:=/d' Makefile

rm -f ./lib/mix/test/fixtures/rebar ./lib/mix/test/fixtures/rebar3
%if %{__with_rebar}
# Do nothing
%else
# Disable rebar-related tests (tests require both rebar and rebar3)
rm -f ./lib/mix/test/mix/rebar_test.exs
touch ./lib/mix/test/fixtures/rebar
%endif %{__with_rebar}

%if %{__with_rebar3}
# Do nothing
%else
# Disable rebar-related tests (tests require both rebar and rebar3)
rm -f ./lib/mix/test/mix/rebar_test.exs
touch ./lib/mix/test/fixtures/rebar3
%endif %{__with_rebar3}

%build
export LANG=C.UTF-8
%if %{__with_rebar}
export REBAR=/usr/bin/rebar
export REBAR_DEPS_PREFER_LIBS=TRUE
%endif %{__with_rebar}
%if %{__with_rebar3}
export REBAR3=/usr/bin/rebar3
%endif %{__with_rebar3}
export ERL_LIBS=/usr/share/erlang/lib/
make compile
make build_man

%check
export LANG=C.UTF-8
%if %{__with_rebar}
export REBAR=/usr/bin/rebar
export REBAR_DEPS_PREFER_LIBS=TRUE
%endif %{__with_rebar}
%if %{__with_rebar3}
export REBAR3=/usr/bin/rebar3
%endif %{__with_rebar3}
export ERL_LIBS=/usr/share/erlang/lib/
make test

%install
mkdir -p %{buildroot}/%{_datadir}/%{name}/%{version}
cp -ra bin lib %{buildroot}/%{_datadir}/%{name}/%{version}

mkdir -p %{buildroot}/%{_bindir}
ln -s %{_datadir}/%{name}/%{version}/bin/{elixir,elixirc,iex,mix} %{buildroot}/%{_bindir}/

# Manual pages
mkdir -p %{buildroot}/%{_mandir}/man1
cp -a man/elixir.1 man/elixirc.1 man/iex.1 man/mix.1 %{buildroot}/%{_mandir}/man1

%files
%license LICENSE
%{_bindir}/elixir
%{_bindir}/elixirc
%{_bindir}/iex
%{_bindir}/mix
%{_datadir}/%{name}
%{_mandir}/man1/elixir.1*
%{_mandir}/man1/elixirc.1*
%{_mandir}/man1/iex.1*
%{_mandir}/man1/mix.1*

%package doc
License: ASL 2.0
Summary: Documentation for the elixir language and tools

%description doc
HTML documentation for eex, elixir, iex, logger and mix.

%files doc
%license docs/LICENSE
%doc docs/doc/eex docs/doc/elixir docs/doc/iex docs/doc/logger docs/doc/mix

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.2-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Mar 16 2020 Timothée Floure <fnux@fedoraproject.org> - 1.10.2-1
- New upstream release

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Oct 21 2019 Timothée Floure <fnux@fedoraproject.org> - 1.9.2-1
- New upstream release

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul 20 2019 Peter Lemenkov <lemenkov@gmail.com> - 1.9.1-1
- New upstream release

* Tue Jun 25 2019 Peter Lemenkov <lemenkov@gmail.com> - 1.9.0-1
- New upstream release

* Wed May 15 2019 Timothée Floure <fnux@fedoraproject.org> - 1.8.2-1
- New upstream release

* Tue Apr 16 2019 Peter Lemenkov <lemenkov@gmail.com> - 1.8.1-3
- Disable check for endianness during startup. Apparently this causes issues
  with RabbitMQ (?).

* Thu Mar 07 2019 Peter Lemenkov <lemenkov@gmail.com> - 1.8.1-2
- Let it to be built and tested w/o rebar/rebar3

* Wed Feb 06 2019 Timothée Floure <fnux@fedoraproject.org> - 1.8.1-1
- Update to upstream 1.8.1

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 15 2019 Timothée Floure <fnux@fedoraproject.org> - 1.8.0-1
- New upstream release

* Sun Nov 18 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.7.3-2
- Use C.UTF-8 locale
  See https://fedoraproject.org/wiki/Changes/Remove_glibc-langpacks-all_from_buildroot

* Mon Oct 22 2018 Timothée Floure <fnux@fedoraproject.org> - 1.7.3-1
- New upstream release

* Sun Aug 19 2018 Timothée Floure <fnux@fedoraproject.org> - 1.7.2-1
- New upstream release

* Mon Jul 30 2018 Timothée Floure <fnux@fedoraproject.org> - 1.7.1-1
- New upstream release

* Thu Jul 26 2018 Timothée Floure <fnux@fedoraproject.org> - 1.7.0-1
- New upstream release
- Remove deprecated 'Group' tag

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Peter Lemenkov <lemenkov@gmail.com> - 1.6.6-1
- New upstream release

* Wed Jun 20 2018 Timothée Floure <fnux@fedoraproject.org> - 1.6.5-3
- Fix version-control-internal-file rpmlint errors
- Fix hidden-file-or-dir rpmlint warnings

* Thu Jun 07 2018 Timothée Floure <fnux@fedoraproject.org> - 1.6.5-2
- Switch from the rebar_* macros to upstream's makefile (without forgetting to
  properly set the environment) and fix the build section.
- Backport patch0 from upstream to fix some failing tests.

* Wed May 23 2018 Peter Lemenkov <lemenkov@gmail.com> - 1.6.5-1
- New upstream release

* Wed May 23 2018 Peter Lemenkov <lemenkov@gmail.com> - 1.6.0-1
- New upstream release

* Mon Apr 30 2018 Timothée Floure <fnux@fedoraproject.org> - 1.5.0-4
- Package the man pages of elixir, elixirc, iex and mix.
- Package (elixir-doc subpackage) the HTML documentation of eex, elixir, iex, logger and mix.
- Change the license from ASL 2.0 and ERPL to ASL 2.0 only.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Martin Langhoff <martin@laptop.org> - 1.5.0-1
- New upstream release

* Thu Jul 27 2017 Martin Langhoff <martin@laptop.org> - 1.4.5-2
- Make arch specific, fixes #1470583
- Fix build warnings about locale

* Wed Jul 26 2017 Martin Langhoff <martin@laptop.org> - 1.4.5-1
- New upstream release

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Apr 17 2017 Martin Langhoff <martin@laptop.org> - 1.4.2-1
- New upstream release

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Nov  8 2016 Martin Langhoff <martin@laptop.org> - 1.3.4-1
- New upstream release

* Mon Sep 19 2016 Martin Langhoff <martin@laptop.org> - 1.3.3-1
- New upstream release.

* Thu Sep 1 2016 Martin Langhoff <martin@laptop.org> - 1.3.2-1
- New upstream release

* Tue Jun 28 2016 Martin Langhoff <martin@laptop.org> - 1.3.1-1
- New upstream release

* Fri Jun 24 2016 Martin Langhoff <martin@laptop.org> - 1.3.0-1
- New upstream release

* Fri Jun 10 2016 Martin Langhoff <martin@laptop.org> - 1.2.6-1
- New upstream release 1.2.6

* Fri May 20 2016 Peter Lemenkov <lemenkov@gmail.com> - 1.2.5-2
- Manually specify Requires for now - our dependency generator cannot handle
  noarch packages yet.

* Fri May 20 2016 Peter Lemenkov <lemenkov@gmail.com> - 1.2.5-1
- Ver. 1.2.5

* Mon Apr 4 2016 Martin Langhoff <martin@laptop.org> - 1.2.4-1
- New upstream release.

* Wed Feb 24 2016 Martin Langhoff <martin@laptop.org> - 1.2.3-1
- New upstream release.

* Mon Feb 8 2016 Martin Langhoff <martin@laptop.org> - 1.2.2-1
- New upstream release.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct 29 2015 Ricky Elrod <relrod@redhat.com> - 1.1.1-1
- Latest upstream release.
- Re-enable test suite to see what breaks.

* Tue Jun 30 2015 Jochen Schmitt <Jochen herr-schmitt de> - 1.0.5-1
- New upstream release
- set a UTF-8 locale to build elixir
- Disable test suite

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Feb 13 2015 Jochen Schmitt <Jochen herr-schmitt de> - 1.0.3-1
- New upstream release

* Wed Oct 22 2014 Jochen Schmitt <Jochen herr-schmitt de> - 1.0.2-1
- New upstream release

* Thu Oct  9 2014 Jochen Schmitt <Jochen herr-schmitt de> - 1.0.1-2
- Fix wrong Erlang release specification in the BRs

* Wed Oct 8 2014 Ricky Elrod <relrod@redhat.com> - 1.0.1-1
- Update to upstream 1.0.1.

* Sat Oct  4 2014 Jochen Schmitt <Jochen herr-schmitt de> - 1.0-1
- New upstream release

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Mar 12 2014 Ricky Elrod <codeblock@fedoraproject.org> - 0.12.5-1
- Update to upstream 0.12.5.

* Thu Feb 13 2014 Ricky Elrod <codeblock@fedoraproject.org> - 0.12.4-1
- Update to upstream 0.12.4.

* Tue Feb 4 2014 Ricky Elrod <codeblock@fedoraproject.org> - 0.12.3-1
- Update to upstream 0.12.3.

* Sun Jan 19 2014 Ricky Elrod <codeblock@fedoraproject.org> - 0.12.2-2
- Remove patch that is no longer needed.

* Fri Jan 17 2014 Patrick Uiterwijk <puiterwijk@redhat.com> - 0.12.2-1
- Update to upstream 0.12.2.

* Sat Jan 11 2014 Ricky Elrod <codeblock@fedoraproject.org> - 0.12.1-1
- Update to upstream 0.12.1.

* Sun Dec 15 2013 Ricky Elrod <codeblock@fedoraproject.org> - 0.12.0-1
- Update to upstream 0.12.0.

* Sun Nov 24 2013 Ricky Elrod <codeblock@fedoraproject.org> - 0.11.2-1
- Update to upstream 0.11.2.

* Sat Nov 2 2013 Ricky Elrod <codeblock@fedoraproject.org> - 0.11.0-1
- Update to upstream 0.11.0.

* Tue Oct 8 2013 Ricky Elrod <codeblock@fedoraproject.org> - 0.10.3-1
- Update to upstream 0.10.3.

* Wed Sep 4 2013 Ricky Elrod <codeblock@fedoraproject.org> - 0.10.2-1
- Update to upstream 0.10.2.

* Sun Aug 4 2013 Ricky Elrod <codeblock@fedoraproject.org> - 0.10.1-2
- Copy mix binary, too.

* Sat Aug 3 2013 Ricky Elrod <codeblock@fedoraproject.org> - 0.10.1-1
- Update to upstream 0.10.1.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 16 2013 Ricky Elrod <codeblock@fedoraproject.org> - 0.10.0-1
- Update to upstream 0.10.0.

* Wed Jun 12 2013 Ricky Elrod <codeblock@fedoraproject.org> - 0.9.3-2
- Fix patch, doctest.exs was renamed to doc_test.exs

* Wed Jun 12 2013 Ricky Elrod <codeblock@fedoraproject.org> - 0.9.3-1
- Update to upstream 0.9.3.

* Wed Jun 12 2013 Ricky Elrod <codeblock@fedoraproject.org> - 0.9.1-1
- Update to upstream 0.9.1.
- Clean up specfile.

* Sun Feb 17 2013 Ricky Elrod <codeblock@fedoraproject.org> - 0.8.1-1
- Update to upstream 0.8.1.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 7 2013 Ricky Elrod <codeblock@fedoraproject.org> - 0.7.2-1
- Update to upstream 0.7.2.

* Mon Oct 22 2012 Ricky Elrod <codeblock@fedoraproject.org> - 0.7.0-1.20121022git833e9e9
- Update to upstream 0.7.0.

* Wed Aug 1 2012 Ricky Elrod <codeblock@fedoraproject.org> - 0.6.0-1.20120801git109919c
- Update to upstream 0.6.0.

* Sat May 26 2012 Ricky Elrod <codeblock@fedoraproject.org> - 0.5.0-1.20120526git6052352
- Initial build.
