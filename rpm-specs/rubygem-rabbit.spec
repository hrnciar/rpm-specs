%global	gem_name	rabbit
%define	BothRequires() \
Requires:	%1 \
BuildRequires:	%1 \
%{nil}

Name:		rubygem-%{gem_name}
Version:	3.0.0
Release:	4%{?dist}

Summary:	RD-document-based presentation application
# CC-BY: rubykaigi2011-background-white.jpg and
# rubykaigi2011-background-black.jpg
# (see doc/en/index.rd)
License:	GPLv2+ and CC-BY
URL:		http://rabbit-shocker.org/
Source0:	https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/rabbit-shocker/rabbit.git
# cd rabbit/
# git reset --hard %%{version}
# tar czf rubygem-rabbit-%%{version}-test-missing-files.tar.gz test/fixtures/
Source1:	%{name}-%{version}-test-missing-files.tar.gz
Source10:	rabbit.desktop
Source11:	rabbit.xml
# Rescue kramdown 1
Patch1:	rubygem-rabbit-3.0.0-rescue-kramdown1.patch

%BothRequires	ruby(release)
BuildRequires:	rubygems-devel
Requires:	ruby(rubygems)

%BothRequires	rubygem(coderay)
%BothRequires	rubygem(faraday)
%BothRequires	rubygem(gettext)
%BothRequires	rubygem(gdk_pixbuf2)
%BothRequires	rubygem(gtk3)
%BothRequires	rubygem(hikidoc)
%BothRequires	rubygem(kramdown)
%if 0%{?fedora} >= 32
Requires:	rubygem-kramdown >= 2.0
%BothRequires	rubygem-kramdown-parser-gfm
%else
Requires:	rubygem-kramdown < 1.18
%endif
%BothRequires	rubygem(nokogiri)
%BothRequires	rubygem(poppler)
%BothRequires	rubygem(rouge)
%BothRequires	rubygem(rsvg2)
%BothRequires	rubygem(rdtool)
%BothRequires	rubygem(rttool)
# test_codeblock_fence test needs below
BuildRequires:	%{_bindir}/blockdiag
BuildRequires:	desktop-file-utils
# For rabbirc
Requires:	rubygem(net-irc)
Requires:	rubygem(gdk_pixbuf2) >= 3.0.9

BuildRequires:	rubygem(racc)
BuildRequires:	rubygem(test-unit)
BuildRequires:	rubygem(test-unit-notify)
BuildRequires:	rubygem(test-unit-rr)
BuildRequires:	xorg-x11-server-Xvfb

BuildArch:	noarch
Provides:	rubygem(%{gem_name}) = %{version}

%description
Rabbit is an RD-document-based presentation application.

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description doc
Documentation for %{name}

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
# For now, relax kramdown series dependency
sed -i %{gem_name}.gemspec -e 's|kramdown-parser-gfm|kramdown|'

%patch1 -p1

%build
gem build %{gem_name}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
	%{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

# Desktop, mime, icon
mkdir -p -m 0755 \
	%{buildroot}%{_datadir}/{applications/,mime/packages/}
desktop-file-install \
	--dir=%{buildroot}%{_datadir}/applications/ \
	%{SOURCE10}
install -cpm 644 %{SOURCE11} %{buildroot}%{_datadir}/mime/packages/

mkdir -p -m 0755 \
	%{buildroot}%{_datadir}/icons/hicolor/32x32/apps/
install -cpm 644 .%{gem_instdir}/sample/rabbit_icon.png \
	%{buildroot}%{_datadir}/icons/hicolor/32x32/apps/

# Cleanup
pushd %{buildroot}%{gem_instdir}
rm -rf \
	Gemfile Rakefile %{gem_name}.gemspec \
	po/ \
	test/
popd

%find_lang rabbit
# list directories under %%{gem_instdir}/data/locale/
find %{buildroot}%{gem_instdir}/data/locale -type d | while read dir
do
	echo "%%dir ${dir#%{buildroot}}" >> rabbit.lang
done

%check
# test files are not included in binary rpm, so just
# unpack here
pushd .%{gem_instdir}
gzip -dc %{SOURCE1} | tar -xf -
xvfb-run \
	ruby test/run-test.rb
popd

%files -f rabbit.lang
# rpmlint: keep all zero-length file
%dir	%{gem_instdir}
%doc	%{gem_instdir}/[A-Z]*

%{_bindir}/rabbit-slide
%{_bindir}/rabbit
%{_bindir}/rabbit-theme
%{_bindir}/rabbit-command
%{_bindir}/rabbirc
%{gem_instdir}/bin

%{gem_libdir}
%dir	%{gem_instdir}/data/
%{gem_instdir}/data/account.kou.gpg
%{gem_instdir}/data/rabbit/
%{gem_instdir}/entities/

%{_datadir}/applications/rabbit.desktop
%{_datadir}/mime/packages/rabbit.xml
%{_datadir}/icons/hicolor/32x32/apps/rabbit_icon.png

%exclude	%{gem_cache}
%{gem_spec}

%files doc
%doc	%{gem_docdir}
%doc	%{gem_instdir}/doc/
%dir	%{gem_instdir}/misc/
%{gem_instdir}/misc/*.rb
%doc	%{gem_instdir}/misc/*/
%doc	%{gem_instdir}/sample/	

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.0.0-3
- BR: rubygem(racc) for test

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 13 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.0.0-2
- Stop to use RPM rich dependency - does not seem to do as I expect

* Mon Sep  9 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.0.0-1
- 3.0.0
- Relax kramdown dependency, handle both kramdown 1.17 and 2 case

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.2.1-2
- Remove obsolete scriptlets

* Tue Sep 19 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.2.1-1
- 2.2.1

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 23 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.2.0-1
- 2.2.0

* Wed Jun  8 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.1.9-1
- 2.1.9

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Sep 13 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.1.8-1
- 2.1.8

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Feb 27 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.1.6-1
- 2.1.6

* Tue Feb 24 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.1.4-1
- 2.1.4

* Fri Nov  7 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.1.3-3
- Rescue Encoding::UndefinedConversionError on logger
  (shocker-ja:1228)

* Thu Oct 02 2014 Rex Dieter <rdieter@fedoraproject.org> 2.1.3-2
- update desktop/icon/mime scriptlets

* Wed Aug 13 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.1.3-1
- 2.1.3

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 17 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.1.2-2
- Always call xvfb-run at %%check

* Mon Mar 17 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.1.2-1
- 2.1.2

* Mon Dec 23 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.1.1-3
- Use xvfb-run on F-19

* Mon Dec 23 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.1.1-2
- Require net-irc for rabbirc
- Install desktop and mime, icon

* Sun Nov 17 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.1.1-1
- Initial package
