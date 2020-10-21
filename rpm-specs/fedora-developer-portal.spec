%global debug_package %{nil}
%global commit 7fc490ca015e8ce912acddaea33093541cc870a5
%global content_commit 5d543b8feeb52994064ee41c6a8d96f994460d3b
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global content_shortcommit %(c=%{content_commit}; echo ${c:0:7})
%global gems_dir %(gem environment | grep "USER INSTALLATION" | cut -d: -f2-)

Name:    fedora-developer-portal
Version: 1.0.0
Release: 0.9.git%{shortcommit}%{?dist}
Summary: Fedora Developer Portal
BuildArchitectures: noarch
License: GPLv2+
URL:     https://developer.fedoraproject.org/
Source0: https://github.com/developer-portal/website/archive/%{commit}.tar.gz#/website-%{shortcommit}.tar.gz
Source1: https://github.com/developer-portal/content/archive/%{content_commit}.tar.gz#/content-%{content_shortcommit}.tar.gz
#Source0: %%{name}-%%{shortcommit}.tar.xz
Source2: %{name}
Source3: Gemfile
Source5: https://github.com/frantisekz/jekyll-lunr-js-search/releases/download/3.3.0/jekyll-lunr-js-search-3.3.0.gem
Source6: https://rubygems.org/downloads/jekyll-sitemap-1.4.0.gem
Source7: https://raw.githubusercontent.com/slashdotdash/jekyll-lunr-js-search/842f0b4258a8ffaac70831381373b2f1d3b651a5/build/jekyll_lunr_js_search.rb
Source100: %{name}.desktop
Source101: %{name}.png

Requires: chromium

BuildRequires: desktop-file-utils
BuildRequires: python3-feedparser
BuildRequires: ruby-devel
BuildRequires: zlib-devel
BuildRequires: libxml2-devel
BuildRequires: libxslt-devel
BuildRequires: nodejs
BuildRequires: wget
BuildRequires: procps-ng
BuildRequires: git-core
BuildRequires: rubygem(nokogiri)
BuildRequires: rubygem(rdoc)
BuildRequires: rubygem(ref)
# Deps for bundled gems
BuildRequires: rubygem(execjs)
BuildRequires: rubygem(jekyll-watch)
BuildRequires: rubygem(jekyll-sass-converter)
BuildRequires: rubygem(jekyll-email-protect)
BuildRequires: rubygem(jekyll-git-authors)
BuildRequires: rubygem(json)
BuildRequires: rubygem(bigdecimal)
BuildRequires: rubygem(safe_yaml)
BuildRequires: rubygem(rouge)
BuildRequires: rubygem(pathutil)
BuildRequires: rubygem(mercenary)
BuildRequires: rubygem(kramdown)
BuildRequires: rubygem(colorator)
BuildRequires: rubygem(addressable)
BuildRequires: rubygem(jekyll)
# BuildRequires: rubygem(jekyll-sitemap)
# BuildRequires: rubygem(jekyll-lunr-js-search)
BuildRequires: rubygem(liquid)
BuildRequires: rubygem(racc)

# Deps for rspec tests
BuildRequires: rubygem(rack)
BuildRequires: rubygem(capybara)
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(rspec-core)
BuildRequires: rubygem(rspec-expectations)

%description
Fedora Developer Portal packaged for offline use.

It includes guides to properly set up Fedora for development
of various types of applications ranging from CLI apps through
GUI apps up to Mobile applications. It also covers multiple
programming languages like C, Go, Java, Python and many more.

%prep

%autosetup -n website-%{commit} -a 1
rmdir content
mv -f content-%{content_commit} content

# Install bundled gems
gem install --local %{SOURCE5}
gem install --local %{SOURCE6}

# Remove annoucement about Development Server
rm _includes/announcement.html
touch _includes/announcement.html

# Add Gemfile with racc dependency
cp %{SOURCE3} .

# Temprorary Workaround to not rely on therubyracer
cp %{SOURCE7} _plugins/

%build
# Build the site and start server

jekyll build
jekyll serve --detach
rspec spec || :

# Finally call wget to get static page
mkdir temp_wget
pushd temp_wget
wget --convert-links -e robots=off -r http://127.0.0.1:4000/ || :
mv 127.0.0.1\:4000/ fedora-developer-portal-content-%{shortcommit}

# Kill server in the background
pgrep -f 'jekyll serve --detach' | xargs kill

%install
mkdir -p %buildroot%{_bindir}
mkdir -p %{buildroot}%{_usr}/share/%{name}
mkdir -p %{buildroot}%{_datadir}/pixmaps/
mkdir -p %{buildroot}%{_datadir}/applications/

cp -af %{SOURCE100} %{buildroot}%{_datadir}/applications/fedora-developer-portal.desktop
cp -af %{SOURCE101} %{buildroot}%{_datadir}/pixmaps/fedora-developer-portal.png
cp %{SOURCE2} %buildroot%{_bindir}/%{name}
install -d %{buildroot}%{_libdir}/%{name}
install -d %{buildroot}%{_bindir}

pushd %{_builddir}/website-%{commit}/temp_wget/fedora-developer-portal-content-%{shortcommit}

cp -Ra * %{buildroot}%{_usr}/share/%{name}

# Validate .desktop file
desktop-file-validate %{buildroot}%{_datadir}/applications/fedora-developer-portal.desktop

%files
%{_bindir}/%{name}
%{_usr}/share/%{name}/
%{_datadir}/applications/fedora-developer-portal.desktop
%{_datadir}/pixmaps/fedora-developer-portal.png

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.9.git7fc490c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Apr 21 2020 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.0.0-0.8.git7fc490c
- Don't advertise support for editing text files (mcatanzaro)

* Thu Mar 26 2020 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.0.0-0.7.git7fc490c
- Use more deps from Fedora repos instead of bundling
- Fix FTBFS
- Use chromium instead of epiphany-runtime

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.6.git7fc490c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.5.git7fc490c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 13 2019 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.0.0-0.4.git7fc490c
- Update content and website
- Add gem: jekyll-git-authors
- Use python3-feedparser

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.3.gitdf5b5f6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.2.gitdf5b5f6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 14 2018 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.0.0-0.1.gitdf5b5f6
- Update website/content
- Drop ExclusiveArch
- Drop bundled BuildRequires: jekyll, liquid
- Run rspec spec during the build

* Thu Mar 15 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.9.4-0.6.git167ae09
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Tue Feb 06 2018 Frantisek Zatloukal <fzatlouk@redhat.com> - 0.9.4-0.5.git167ae09
- Drop dependency on therubyracer and v8
- New BuildRequires: rubygem(execjs)

* Tue Oct 17 2017 Frantisek Zatloukal <fzatlouk@redhat.com> - 0.9.4-0.4.git167ae09
- Work around koji not detecting jekyll binary after installing it via gem

* Thu Oct 12 2017 Frantisek Zatloukal <fzatlouk@redhat.com> - 0.9.4-0.3.git167ae09
- Bundle rubygem-jekyll, rubygem-jekyll-sitemap and rubygem-liquid

* Tue Jul 25 2017 Frantisek Zatloukal <fzatlouk@redhat.com> - 0.9.4-0.2.git167ae09
- Mark package as ExclusiveArch: ix86 x86_64 because of build time libv8 bundle

* Mon Jul 24 2017 Frantisek Zatloukal <fzatlouk@redhat.com> - 0.9.4-0.1.git167ae09
- Bump version
- Use remote URLs for website and content archives

* Mon Jul 24 2017 Frantisek Zatloukal <fzatlouk@redhat.com> - 0.9.3-0.5.git167ae09
- bundle few gems: libv8, therubyracer, jekyll-lunr-js-search

* Thu Jul 20 2017 Frantisek Zatloukal <fzatlouk@redhat.com> - 0.9.3-0.4.git167ae09
- Drop gem install from %prep in favor of BuildRequires
- Use global instead of define

* Wed Jul 19 2017 Frantisek Zatloukal <fzatlouk@redhat.com> - 0.9.3-0.3.git167ae09
- Small changes to spec file

* Thu Jul 13 2017 Frantisek Zatloukal <fzatlouk@redhat.com> - 0.9.3-0.2.git167ae09
- Add .desktop file check
- Update description

* Tue Jul 11 2017 Frantisek Zatloukal <fzatlouk@redhat.com> - 0.9.3-0.1.git167ae09
- Bump requested epiphany-runtime version
- Refactor content fetching and do not rely on manual content tar creation

* Tue Jun 21 2016 Frantisek Zatloukal <fzatlouk@redhat.com> - 0.9.2-1
- Depend on epiphany-runtime instead of epiphany
- Correct upstream url
- Allow running outside the GNOME

* Wed Jun 1 2016 Frantisek Zatloukal <fzatlouk@redhat.com> - 0.9.1-1
- Release 0.9.1
- Add correct workaround for https://bugzilla.gnome.org/show_bug.cgi?id=767101
- Mark package as noarch as it doesn't contain any compiled binary

* Wed Jun 1 2016 Frantisek Zatloukal <fzatlouk@redhat.com> - 0.9.0-1
- Release 0.9.0
- Drop electron in favour of Epiphany

* Tue May 31 2016 Frantisek Zatloukal <fzatlouk@redhat.com> - 0.1.2-1
- Release 0.1.2
- Follow packaging guidelines
- Remove development warning
- Sync with upstream

* Tue May 31 2016 Frantisek Zatloukal <fzatlouk@redhat.com> - 0.1.1-1
- Release 0.1.1
- Add Icon

* Mon May 30 2016 Frantisek Zatloukal <fzatlouk@redhat.com> - 0.1.0-1
- Release 0.1.0
- Unbundle Electron
- Run even in offline mode

* Thu May 12 2016 Frantisek Zatloukal <fzatlouk@redhat.com> - 0.0.1-1
- Release 0.0.1
