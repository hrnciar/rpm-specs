%bcond_with autoreconf
%bcond_with authorcheck
%bcond_with el6_ix86

# Unbundling helper macro
# %1 is the path to dir bundling files (from)
# %2 is the path to dir containing original files (with)
%global unbundle_from_with() \
  bundled_dir="%{buildroot}%1" \
  bundled_files="$(find "${bundled_dir}" -maxdepth 1 -type f -printf '%f\\n')" \
  original_dir="%2" \
  for file in ${bundled_files} \
  do \
    if [ -f "${original_dir}/${file}" ] \
    then \
      rm -f "${bundled_dir}/${file}" \
      ln -s "${original_dir}/${file}" "${bundled_dir}/${file}" \
    fi \
  done

# Bundled Fonts
#
# EL7 version (4.1.0) is missing some icons
%global unbundle_fontawesome       0%{?fedora}%{?el6}
# Not available for EL
%global unbundle_raleway           0%{?fedora}
#
%global unbundle_foundation_icons  0%{?fedora}%{?el6}%{?el7}

# Bundled javascripts
#
# Not available
%global unbundle_foundation        0
# Not available for EL
%global unbundle_html5shiv         0%{?f31}%{?f32}
# Not available for EL
%global unbundle_jquery            0%{?fedora}
# Available version is too old
%global unbundle_jquery_migrate    0
# Not available
%global unbundle_jquery_minicolors 0
# Not available for EL6
%global unbundle_jquery_ui         0%{?fedora}%{?el7}
# Only available for Fedora
%global unbundle_jqplot            0%{?f31}%{?f32}
#
%global unbundle_respond           0%{?f31}%{?f32}%{?el6}%{?el7}

# Licenses
# Sympa itself is GPLv2+.
# Possibly bundled fonts are :
# - fontawesome-fonts :      OFL
# - fontawesome-fonts-web:   OFL and MIT
# - impallari-raleway-fonts: OFL
# - foundation-icons-fonts:  MIT
# Possibly bundled javascripts are :
# - js-html5shiv:            MIT or GPLv2
# - js-jquery-jqplot:        MIT or GPLv2
# - js-jquery:               MIT
# - js-respond:              MIT
# - js-jquery-ui:            MIT
# - js-foundation:           MIT
# - js-jquery-migrate:       MIT
# - js-jquery-minicolors:    MIT
%global licenses_bundled     %{nil} 
# OFL and MIT
%if ! %{unbundle_fontawesome}
%global licenses_bundled %{licenses_bundled} and (OFL and MIT)
%endif
# OFL
%if ! %{unbundle_raleway}
%global licenses_bundled %{licenses_bundled} and OFL
%endif
# MIT
%if ! %{unbundle_foundation_icons} || ! %{unbundle_foundation} || ! %{unbundle_jquery} || ! %{unbundle_jquery_migrate} || ! %{unbundle_jquery_minicolors} || ! %{unbundle_jquery_ui} || ! %{unbundle_respond}
%global licenses_bundled %{licenses_bundled} and MIT
%endif
# MIT or GPLv2
%if ! %{unbundle_html5shiv} || ! %{unbundle_jqplot}
%global licenses_bundled %{licenses_bundled} and (MIT or GPLv2)
%endif


%if 0%{?fedora} || 0%{?rhel} >= 7
%global use_systemd 1
%else
%global use_systemd 0
%endif

%global static_content %{_datadir}/sympa/static_content

#global pre_rel b.2

Name:        sympa
Version:     6.2.58
Release:     %{?pre_rel:0.}1%{?pre_rel:.%pre_rel}%{?dist}
Summary:     Powerful multilingual List Manager
Summary(fr): Gestionnaire de listes électroniques
Summary(ja): 高機能で多言語対応のメーリングリスト管理ソフトウェア
# The License: tag depends on bundled code for a given distro/release
License:     GPLv2+%{licenses_bundled}
URL:         http://www.sympa.org
Source0:     https://github.com/sympa-community/sympa/releases/download/%{version}%{?pre_rel}/%{name}-%{version}%{?pre_rel}.tar.gz

Source100:   sympa-httpd22-fcgid.conf
Source101:   sympa-httpd24-spawn_fcgi.conf
Source102:   sympa-lighttpd.conf
Source103:   sympa-nginx-spawn_fcgi.conf
Source104:   sympa-wwsympa.init
Source105:   sympa-sympasoap.init
Source106:   sympa-rsyslog.conf
Source107:   sympa-logrotate.conf
Source112:   sympa-sysvinit-README.RPM.md
Source113:   sympa-systemd-README.RPM.md
Source114:   aliases.sympa.sendmail
Source115:   aliases.sympa.postfix
Source129:   sympa.service.d-dependencies.conf
Source130:   sympa-sysconfig

# Add path to MHonArc::UTF8 so that sympa_wizard won't miss it
Patch5:      sympa-6.2.36-wizard-mhonarc.patch
# RPM specific customization of site defaults
Patch13:     sympa-6.2.57b.1-confdef.patch
# Disable sympa service by default
Patch14:     sympa-6.2-initdefault.patch

BuildRequires: gcc, make
BuildRequires: gettext
%if %{use_systemd}
BuildRequires: systemd
%endif

# Only for development
%if %{with autoreconf}
BuildRequires: autoconf, automake, gettext-devel
%endif

BuildRequires: perl-generators
# install & check
BuildRequires: perl(Archive::Zip)
BuildRequires: perl(base)
BuildRequires: perl(Carp)
BuildRequires: perl(CGI::Cookie)
BuildRequires: perl(CGI::Fast)
BuildRequires: perl(CGI::Util)
BuildRequires: perl(Class::Singleton)
BuildRequires: perl(Config)
BuildRequires: perl(constant)
BuildRequires: perl(Cwd)
BuildRequires: perl(Data::Password)
BuildRequires: perl(DateTime)
BuildRequires: perl(DateTime::Format::Mail)
BuildRequires: perl(DBD::SQLite)
BuildRequires: perl(DBI)
BuildRequires: perl(Digest::MD5)
BuildRequires: perl(Encode)
BuildRequires: perl(Encode::MIME::Header)
BuildRequires: perl(English)
BuildRequires: perl(FCGI)
BuildRequires: perl(Fcntl)
BuildRequires: perl(feature)
BuildRequires: perl(File::Copy)
BuildRequires: perl(File::Copy::Recursive)
BuildRequires: perl(File::Find)
BuildRequires: perl(File::NFSLock)
BuildRequires: perl(File::Path)
BuildRequires: perl(File::stat)
BuildRequires: perl(File::Temp)
BuildRequires: perl(Getopt::Long)
BuildRequires: perl(HTML::Entities)
BuildRequires: perl(HTML::FormatText)
BuildRequires: perl(HTML::Parser)
BuildRequires: perl(HTML::StripScripts::Parser)
BuildRequires: perl(HTML::TreeBuilder)
BuildRequires: perl(HTTP::Request)
BuildRequires: perl(if)
BuildRequires: perl(IO::File)
BuildRequires: perl(IO::Scalar)
%if 0%{?el6}
BuildRequires: perl(IO::Socket::INET6)
%else
BuildRequires: perl(IO::Socket::IP)
%endif
BuildRequires: perl(IO::Socket::SSL)
BuildRequires: perl(lib)
BuildRequires: perl(Locale::Messages)
BuildRequires: perl(LWP::Protocol::https)
BuildRequires: perl(LWP::UserAgent)
BuildRequires: perl(Mail::Address)
BuildRequires: perl(MIME::Base64)
BuildRequires: perl(MIME::Charset)
BuildRequires: perl(MIME::EncWords)
BuildRequires: perl(MIME::Entity)
BuildRequires: perl(MIME::Head)
BuildRequires: perl(MIME::Lite::HTML)
BuildRequires: perl(MIME::Parser)
BuildRequires: perl(MIME::Tools)
BuildRequires: perl(Net::CIDR)
BuildRequires: perl(Net::LDAP)
BuildRequires: perl(POSIX)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(SOAP::Lite)
BuildRequires: perl(SOAP::Transport::HTTP)
BuildRequires: perl(Socket6)
BuildRequires: perl(Storable)
BuildRequires: perl(strict)
BuildRequires: perl(Sys::Hostname)
BuildRequires: perl(Sys::Syslog)
BuildRequires: perl(Template)
BuildRequires: perl(Term::ProgressBar)
BuildRequires: perl(Test::Compile)
BuildRequires: perl(Test::Harness)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::Pod)
BuildRequires: perl(Text::LineFold)
BuildRequires: perl(Time::HiRes)
BuildRequires: perl(Time::Local)
# For Perl prior to 5.16.0.
%if 0%{?rhel} == 6
BuildRequires: perl(Unicode::CaseFold)
%endif
BuildRequires: perl(Unicode::GCString)
BuildRequires: perl(Unicode::Normalize)
BuildRequires: perl(Unicode::UTF8)
BuildRequires: perl(URI)
BuildRequires: perl(URI::Escape)
BuildRequires: perl(warnings)
BuildRequires: perl(XML::LibXML)

# authorcheck
%if %{with authorcheck}
BuildRequires: perl(Test::Fixme)
BuildRequires: perl(Test::Perl::Critic)
BuildRequires: perl(Test::Pod::Coverage)
BuildRequires: perl(Test::Pod::Spelling::CommonMistakes)
%endif

Requires(pre): shadow-utils

%if ! %{use_systemd}
Requires(post):   chkconfig
Requires(preun):  chkconfig
Requires(preun):  initscripts
Requires(postun): initscripts
%endif

Requires:    smtpdaemon
Requires:    mhonarc
Requires:    perl(DBD::mysql)
Requires:    perl(FCGI)

# Missing Requires on EL6 and EL7
%if 0%{?el6}%{?el7}
Requires:    perl(HTML::FormatText)
Requires:    perl(HTML::StripScripts::Parser)
%endif

# Optional CPAN packages
Requires:    perl(AuthCAS)
Requires:    perl(Clone)
Requires:    perl(Crypt::CipherSaber)
Requires:    perl(Crypt::Eksblowfish)
Requires:    perl(Crypt::OpenSSL::X509)
Requires:    perl(Crypt::SMIME)
Requires:    perl(Data::Password)
Requires:    perl(DateTime::TimeZone)
Requires:    perl(DBD::CSV)
Requires:    perl(Encode::Locale)
# Recommended for handling Japanese vendor codepages.
Requires:    perl(Encode::EUCJPASCII)
# Handling several Chinese standards.
Requires:    perl(Encode::HanExtra)
%if 0%{?el6}
Requires:    perl(IO::Socket::INET6)
%else
Requires:    perl(IO::Socket::IP)
%endif
Requires:    perl(IO::Socket::SSL)
Requires:    perl(List::Util::XS)
Requires:    perl(LWP::Protocol::https)
Requires:    perl(Mail::DKIM::Verifier)
Requires:    perl(Net::DNS)
Requires:    perl(Net::SMTP)
Requires:    perl(Socket6)
# for Perl prior to 5.16.0.
%if 0%{?rhel} == 6
Requires:    perl(Unicode::CaseFold)
%endif
Requires:    perl(Unicode::Normalize)
Requires:    perl(Unicode::UTF8)

# Bundled fonts
%if %{unbundle_fontawesome}
BuildRequires: fontawesome-fonts-web >= 4.3.0
Requires:      fontawesome-fonts-web >= 4.3.0
%else
Provides:      bundled(fontawesome-fonts) = 4.3.0
%endif
%if %{unbundle_raleway}
BuildRequires: impallari-raleway-fonts >= 3.0
Requires:      impallari-raleway-fonts >= 3.0
%else
Provides:      bundled(impallari-raleway-fonts) = 3.0
%endif
%if %{unbundle_foundation_icons}
BuildRequires: foundation-icons-fonts >= 3.0
Requires:      foundation-icons-fonts >= 3.0
%else
Provides:      bundled(foundation-icons-fonts) = 3.0
%endif

# Bundled javascript libs
# foundation
%if %{unbundle_foundation}
BuildRequires: js-foundation6 >= 6.4.2
Requires:      js-foundation6 >= 6.4.2
%else
Provides:      bundled(js-foundation) = 6.4.2
# Bundled in bundled js-foundation
Provides:      bundled(js-what-input) = 4.2.0
%endif
# html5shiv
%if %{unbundle_html5shiv}
BuildRequires: js-html5shiv >= 3.7.2
Requires:      js-html5shiv >= 3.7.2
%else
Provides:      bundled(js-html5shiv) = 3.7.2
%endif
# jquery
%if %{unbundle_jquery}
BuildRequires: js-jquery3 >= 3.2.1
Requires:      js-jquery3 >= 3.2.1
%else
Provides:      bundled(js-jquery) = 3.2.1
%endif
# jquery-migrate
%if %{unbundle_jquery_migrate}
%if 0%{?el7}
BuildRequires: python-XStatic-JQuery-Migrate >= 1.4.1
Requires:      python-XStatic-JQuery-Migrate >= 1.4.1
%else
BuildRequires: xstatic-jquery-migrate-common >= 1.4.1
Requires:      xstatic-jquery-migrate-common >= 1.4.1
%endif
%else
Provides:      bundled(js-jquery-migrate) = 1.4.1
%endif
# jquery-minicolors
%if %{unbundle_jquery_minicolors}
BuildRequires: js-jquery-minicolors >= 2.3.1
Requires:      js-jquery-minicolors >= 2.3.1
%else
Provides:      bundled(js-jquery-minicolors) = 2.3.1
%endif
# jquery-ui
%if %{unbundle_jquery_ui}
%if 0%{?el7}
BuildRequires: python-XStatic-jquery-ui >= 1.12.0
Requires:      python-XStatic-jquery-ui >= 1.12.0
%else
BuildRequires: xstatic-jquery-ui-common >= 1.12.0
Requires:      xstatic-jquery-ui-common >= 1.12.0
%endif
%else
Provides:      bundled(js-jquery-ui) = 1.12.1
%endif
# jqplot
%if %{unbundle_jqplot}
BuildRequires: js-jquery-jqplot >= 1.0.8
Requires:      js-jquery-jqplot >= 1.0.8
%else
Provides:      bundled(js-jquery-jqplot) = 1.0.8
%endif
# respond
%if %{unbundle_respond}
BuildRequires: js-respond >= 1.4.2
Requires:      js-respond >= 1.4.2
%else
Provides:      bundled(js-respond) = 1.4.2
%endif

# perl-libintl-perl for perl(Locale::Messages) is missing on EL6 i386
# RHBZ#1731149
%if ! %{with el6_ix86}
%{?el6:ExcludeArch:  %{ix86}}
%endif


%if 0%{?fedora} || 0%{?rhel} >= 7
%{?perl_default_filter}
%global __requires_exclude perl\\(Conf\\)
%global __provides_exclude perl\\(Conf\\)
%endif

%if 0%{?rhel} == 6
%filter_from_provides /perl(Conf)/d
%filter_from_requires /perl(Conf)/d
%filter_setup
%endif


%description
Sympa is scalable and highly customizable mailing list manager. It
can cope with big lists (200,000 subscribers) and comes with a
complete (user and admin) Web interface. It is internationalized,
and supports the us, fr, de, es, it, fi, and chinese locales. A
scripting language allows you to extend the behavior of commands.
Sympa can be linked to an LDAP directory or an RDBMS to create
dynamic mailing lists. Sympa provides S/MIME-based authentication
and encryption.

%description -l ja
Sympa はスケーラブルで高いカスタマイズ性を持つメーリングリスト管理
ソフトウェアです。巨大なリスト (登録者数 200,000) にも適用でき、完
全な (一般ユーザ用および管理者用) ウェブインタフェースをそなえてい
ます。国際化されており、多数の言語に対応します。内蔵のスクリプティ
ング言語でコマンドの動作を拡張できます。Sympa はまた、LDAP ディレ
クトリや RDBMS と連携して動的なメーリングリストを作成できます。ま
た、S/MIME に基づく認証や暗号化もできます。


%package httpd
Summary:  Sympa with Apache HTTP Server
Summary(fr): Sympa avec Serveur HTTP Apache
Summary(ja): SympaのApache HTTP Server対応
Requires: %{name} = %{version}-%{release}
Requires: httpd
%if 0%{?fedora} || 0%{?rhel} >= 7
Requires: spawn-fcgi
%else
Requires: mod_fcgid
%endif
Conflicts: %{name}-lighttpd, %{name}-nginx

%description httpd
Apache HTTP Server support for Sympa.

%description httpd -l ja
Sympa の Apache HTTP Server 対応。


%package lighttpd
Summary:  Sympa with lighttpd
Summary(fr): Sympa avec lighttpd
Summary(ja): Sympaのlighttpd対応
Requires: %{name} = %{version}-%{release}
Requires: lighttpd
Requires: lighttpd-fastcgi
Conflicts: %{name}-httpd, %{name}-nginx

%description lighttpd
lighttpd support for Sympa.

%description lighttpd -l ja
Sympa の lighttpd 対応。


%package nginx
Summary:  Sympa with nginx
Summary(fr): Sympa avec nginx
Summary(ja): Sympaのnginx対応
Requires: %{name} = %{version}-%{release}
Requires: nginx
Requires: spawn-fcgi
Conflicts: %{name}-httpd, %{name}-lighttpd

%description nginx
nginx support for Sympa.

%description nginx -l ja
Sympa の nginx 対応。


%package devel-doc
Summary: Sympa devel doc
Requires: %{name} = %{version}-%{release}

%description devel-doc
Sympa documentation for developers.


%prep
%setup -q -n %{name}-%{version}%{?pre_rel}
%patch5 -p0 -b .mhonarc
%patch13 -p0 -b .confdef
%patch14 -p0 -b .initdefault


%build
# Development
%if %{with autoreconf}
autoreconf --install
%endif

# Give install "-p" preserving mtime to prevent unexpected update of CSS.
%configure \
    --enable-fhs \
    --prefix=%{_prefix} \
    --bindir=%{_libexecdir}/sympa \
    --docdir=%{_docdir}/%{name} \
    --libexecdir=%{_libexecdir}/sympa \
    --localstatedir=%{_localstatedir} \
    --sysconfdir=%{_sysconfdir}/sympa \
    --with-cgidir=%{_libexecdir}/sympa \
    --with-confdir=%{_sysconfdir}/sympa \
%if %{use_systemd}
    --without-initdir \
    --with-unitsdir=%{_unitdir} \
    --with-piddir=%{_rundir}/sympa \
%else
    --with-initdir=%{_initrddir} \
    --with-piddir=%{_localstatedir}/run/sympa/ \
%endif
    --with-smrshdir=%{_sysconfdir}/smrsh \
    --with-aliases_file=%{_localstatedir}/lib/sympa/sympa_aliases \
    --with-perl=%{_bindir}/perl \
    --with-staticdir=%{static_content} \
    --with-cssdir=%{_localstatedir}/lib/sympa/css \
    --with-picturesdir=%{_localstatedir}/lib/sympa/pictures \
    INSTALL_DATA='install -c -p -m 644'
%make_build

# cancel workaround in Makefile getting previous version.
rm -f previous_sympa_version

pushd po/sympa; rm -f stamp-po; make; popd
pushd po/web_help; rm -f stamp-po; make; popd


%install
%make_install

%find_lang %{name}
%find_lang web_help

# Unbundle fonts from static_content/fonts
# font-awesome
%if %{unbundle_fontawesome}
%unbundle_from_with %{static_content}/fonts/font-awesome/fonts %{_datadir}/fonts/fontawesome
%unbundle_from_with %{static_content}/fonts/font-awesome/css %{_datadir}/font-awesome-web/css
%endif

# Raleway
%if %{unbundle_raleway}
rm -f %{buildroot}%{static_content}/fonts/Raleway/OFL.txt
%unbundle_from_with %{static_content}/fonts/Raleway %{_datadir}/fonts/impallari-raleway
%endif

# foundation-icons
%if %{unbundle_foundation_icons}
rm -f %{buildroot}%{_datadir}/fonts/foundation-icons/preview.html
rm -f %{buildroot}%{_datadir}/fonts/foundation-icons/foundation-icons.{eot,svg,woff}
rm -rf %{buildroot}%{_datadir}/fonts/foundation-icons/svgs
%unbundle_from_with %{static_content}/fonts/foundation-icons %{_datadir}/fonts/foundation-icons
%endif

# Unbundle javascript libraries from static_content/js
# FIXME : foundation (Foundation for Sites 6, with float grid support)
%if %{unbundle_foundation}
%unbundle_from_with %{static_content}/js/foundation/js %{_datadir}/javascript/foundation/js
%unbundle_from_with %{static_content}/js/foundation/css %{_datadir}/javascript/foundation/css
# what-input.js
%unbundle_from_with %{static_content}/js/foundation/js/vendor %{_datadir}/javascript
%endif

# html5shiv
%if %{unbundle_html5shiv}
%unbundle_from_with %{static_content}/js/html5shiv %{_datadir}/javascript
%endif

# jquery
%if %{unbundle_jquery}
%unbundle_from_with %{static_content}/js %{_datadir}/javascript/jquery/3
%endif

# FIXME : jquery-migrate
%if %{unbundle_jquery_migrate}
%unbundle_from_with %{static_content}/js %{_datadir}/javascript/jquery_migrate
%endif

# FIXME : jquery-minicolors
%if %{unbundle_jquery_minicolors}
%unbundle_from_with %{static_content}/js/jquery-minicolors %{_datadir}/javascript/jquery-minicolors
%endif

# jquery-ui
%if %{unbundle_jquery_ui}
%unbundle_from_with %{static_content}/js/jquery-ui %{_datadir}/javascript/jquery_ui
# FIXME: Unbundle theme (smoothness ?)
#unbundle_from_with %{static_content}/js/jquery-ui/images %{_datadir}/javascript/jquery_ui/themes/smoothness/images
%endif

# jqplot
%if %{unbundle_jqplot}
%unbundle_from_with %{static_content}/js/jqplot %{_datadir}/javascript/jquery-jqplot
%endif

# respond
%if %{unbundle_respond}
%unbundle_from_with %{static_content}/js/respondjs %{_datadir}/javascript
%endif

# Save version info.
mv %{buildroot}%{_sysconfdir}/sympa/data_structure.version \
    %{buildroot}%{_sysconfdir}/sympa/data_structure.current_version

# Copy *httpd config files.
mkdir -p %{buildroot}%{_sysconfdir}/httpd/conf.d
%if 0%{?fedora} || 0%{?rhel} >= 7
install -m 0644 %{SOURCE101} %{buildroot}%{_sysconfdir}/httpd/conf.d/sympa.conf
%else
install -m 0644 %{SOURCE100} %{buildroot}%{_sysconfdir}/httpd/conf.d/sympa.conf
%endif
mkdir -p %{buildroot}%{_sysconfdir}/lighttpd/conf.d
install -m 0644 %{SOURCE102} %{buildroot}%{_sysconfdir}/lighttpd/conf.d/sympa.conf
mkdir -p %{buildroot}%{_sysconfdir}/nginx/conf.d
install -m 0644 %{SOURCE103} %{buildroot}%{_sysconfdir}/nginx/conf.d/sympa.conf

# Copy init scripts or unit files for nginx/spawn-fcgi etc.
%if %{use_systemd}
install -m 0644 src/etc/script/wwsympa.service \
    %{buildroot}%{_unitdir}/wwsympa.service
install -m 0644 src/etc/script/sympasoap.service \
    %{buildroot}%{_unitdir}/sympasoap.service
mkdir -p %{buildroot}%{_tmpfilesdir}
install -m 0644 src/etc/script/sympa-tmpfiles.conf \
    %{buildroot}%{_tmpfilesdir}/sympa.conf
mkdir -p %{buildroot}%{_sysconfdir}/systemd/system/sympa.service.d
install -m 0644 %{SOURCE129} \
    %{buildroot}%{_sysconfdir}/systemd/system/sympa.service.d/dependencies.conf
%else
install -m 0755 %{SOURCE104} %{buildroot}%{_initrddir}/wwsympa
install -m 0755 %{SOURCE105} %{buildroot}%{_initrddir}/sympasoap
%endif

# Copy system config file.
mkdir -p %{buildroot}%{_sysconfdir}/sysconfig
install -m 0644 %{SOURCE130} %{buildroot}%{_sysconfdir}/sysconfig/sympa

# Copy docs.
mv %{buildroot}%{_docdir}/%{name} __doc
cp -p AUTHORS.md CONTRIBUTING.md NEWS.md README.md __doc/
%if %{use_systemd}
cp -p %{SOURCE113} __doc/README.RPM.md
%else
cp -p %{SOURCE112} __doc/README.RPM.md
%endif
mv %{buildroot}%{_sysconfdir}/sympa/README __doc/
%if 0%{?el6}%{?el7}
ln -s %{_datadir}/doc/%{name}-%{version}/README \
    %{buildroot}/%{_sysconfdir}/sympa/README
ln -s %{_datadir}/doc/%{name}-%{version}/README \
    %{buildroot}/%{_datadir}/sympa/default/README
%else
ln -s %{_datadir}/doc/%{name}/README \
    %{buildroot}/%{_sysconfdir}/sympa/README
ln -s %{_datadir}/doc/%{name}/README \
    %{buildroot}/%{_datadir}/sympa/default/README
%endif
mv %{buildroot}%{_sysconfdir}/sympa/sympa.conf-dist __doc/

# Copy robot aliases.
install -m 0644 %{SOURCE114} %{SOURCE115} %{buildroot}%{_sysconfdir}/sympa/
touch %{buildroot}%{_sysconfdir}/sympa/aliases.sympa.sendmail.db
touch %{buildroot}%{_sysconfdir}/sympa/aliases.sympa.postfix.db

# Copy rsyslog config
mkdir -p %{buildroot}%{_sysconfdir}/rsyslog.d
install -m 0644 %{SOURCE106} %{buildroot}%{_sysconfdir}/rsyslog.d/sympa.conf

# Create logrotate item
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d
install -m 0644 %{SOURCE107} %{buildroot}%{_sysconfdir}/logrotate.d/sympa

# Create configuration override structure
for conffile in \
    auth.conf charset.conf crawlers_detection.conf create_list.conf \
    edit_list.conf nrcpt_by_domain.conf topics.conf \
    mime.types sympa.wsdl ;
    do cp -a %{buildroot}%{_datadir}/%{name}/default/$conffile \
        %{buildroot}%{_sysconfdir}/%{name}/;
done

# Create directory for S/MIME user certificates
mkdir -p %{buildroot}%{_localstatedir}/lib/sympa/X509-user-certs


%check
make check
%if %{with authorcheck}
make authorcheck || true
%endif


%pre
# Create "sympa" group if it does not exist
getent group sympa >/dev/null || /usr/sbin/groupadd -r sympa

# Create "sympa" user if it does not exist
getent passwd sympa >/dev/null || \
  /usr/sbin/useradd -r -g sympa \
      -d %{_localstatedir}/lib/sympa \
      -c "System User for Sympa" \
      -s "/sbin/nologin" \
      sympa

# Fix CSS and pictures paths
if [ $1 -gt 1 ]; then
    if [ -d %{_localstatedir}/lib/%{name}/static_content/css ]; then
        mv -fu %{_localstatedir}/lib/%{name}/static_content/css/* \
            %{_localstatedir}/lib/%{name}/css/ \
            && rm -rf %{_localstatedir}/lib/%{name}/static_content/css/
    fi
    if [ -d %{_localstatedir}/lib/%{name}/static_content/pictures ]; then
        mv -fu %{_localstatedir}/lib/%{name}/static_content/pictures/* \
            %{_localstatedir}/lib/%{name}/pictures/ \
            && rm -rf %{_localstatedir}/lib/%{name}/static_content/pictures/
    fi
    if [ ! -d %{_localstatedir}/lib/%{name}/static_content/css \
        -a ! -d %{_localstatedir}/lib/%{name}/static_content/pictures \
        -a -d %{_localstatedir}/lib/%{name}/static_content ]; then
        rm -r %{_localstatedir}/lib/%{name}/static_content/
    fi
fi
exit 0


%post
# register service
%if %{use_systemd}
%systemd_post sympa.service
%else
/sbin/chkconfig --add sympa
%endif

# create cookie
function create_cookie {
    cook=`mktemp`
    perl -ne 'chomp $_; print $1 if /^cookie\s+(\S.*)/' \
        %{_sysconfdir}/sympa/sympa.conf > $cook
    if [ '!' -s $cook ]; then
        if [ -e %{_sysconfdir}/sympa/cookies.history ]; then
            cp -p %{_sysconfdir}/sympa/cookies.history $cook
        else
            dd if=/dev/urandom bs=2048 count=1 2>/dev/null | md5sum | \
            cut -d" " -f1 > $cook
        fi
        perl -i -pe '/^#cookie\s/ and $_ = "cookie ".`cat '$cook'`."\n"' \
            %{_sysconfdir}/sympa/sympa.conf
    fi
    rm -f $cook
}

# create config at first time.
function create_config {
    ## create site configurations
    if [ '!' -e %{_sysconfdir}/sympa/data_structure.version ]; then
        cp -p %{_sysconfdir}/sympa/data_structure.current_version \
            %{_sysconfdir}/sympa/data_structure.version
    fi
    ## create sympa_aliases
    if [ '!' -e %{_localstatedir}/lib/sympa/sympa_aliases ]; then
        touch %{_localstatedir}/lib/sympa/sympa_aliases
        chown sympa:sympa %{_localstatedir}/lib/sympa/sympa_aliases
        chmod 644 %{_localstatedir}/lib/sympa/sympa_aliases
        touch %{_localstatedir}/lib/sympa/sympa_aliases.db
        chown sympa:root %{_localstatedir}/lib/sympa/sympa_aliases.db
        chmod 664 %{_localstatedir}/lib/sympa/sympa_aliases.db
    fi
}

function upgrade_data_structure {
    # Stop sympa if it is running
%if %{use_systemd}
    if systemctl is-active sympa > /dev/null 2>&1; then
        /usr/bin/systemctl stop sympa > /dev/null 2>&1
        ACTIVE="yes"
    fi
%else
    if [ -e %{_localstatedir}/lock/subsys/sympa ]; then
        /sbin/service sympa stop > /dev/null 2>&1
        ACTIVE="yes"
    fi
%endif
    # Upgrade
    rm -f %{_sysconfdir}/sympa/sympa.conf.bin > /dev/null 2>&1
    if %{_sbindir}/sympa.pl --upgrade > /dev/null 2>&1; then
        # Start sympa if it was running previously
        if [ "$ACTIVE" == "yes" ]; then
%if %{use_systemd}
            /usr/bin/systemctl start sympa > /dev/null 2>&1
%else
            /sbin/service sympa start > /dev/null 2>&1
%endif
        fi
    else
        echo ============================================================
        echo Notice: Failed upgrading data structure.  See logfile.
        echo Sympa is stopped.
        echo ============================================================
    fi
}

# Install
if [ $1 -eq 1 ]; then
    create_cookie
    create_config
    echo ============================================================
    echo Sympa had been installed successfully.  If you installed
    echo Sympa at first time, please read:
    echo %{_docdir}/%{name}-%{version}/README.RPM.md
    echo ============================================================
fi

# Update
if [ $1 -gt 1 ]; then
    upgrade_data_structure
fi


%preun
%if %{use_systemd}
%systemd_preun sympa.service
%else
if [ $1 -eq 0 ] ; then
    /sbin/service sympa stop >/dev/null 2>&1
    /sbin/chkconfig --del sympa
fi
%endif


%postun
%if %{use_systemd}
%systemd_postun_with_restart sympa.service
%else
if [ "$1" -ge "1" ] ; then
    /sbin/service sympa condrestart >/dev/null 2>&1 || :
fi
%endif

# httpd
%if 0%{?fedora} || 0%{?rhel} >= 7
%post httpd
# register service
%systemd_post wwsympa.service
%systemd_post sympasoap.service
%endif

%if 0%{?fedora} || 0%{?rhel} >= 7
%preun httpd
%systemd_preun wwsympa.service
%systemd_preun sympasoap.service
%endif

%if 0%{?fedora} || 0%{?rhel} >= 7
%postun httpd
%systemd_postun_with_restart wwsympa.service
%systemd_postun_with_restart sympasoap.service
%endif


# nginx
%preun nginx
%if %{use_systemd}
%systemd_preun wwsympa.service
%systemd_preun sympasoap.service
%else
if [ $1 -eq 0 ] ; then
    /sbin/service wwsympa stop >/dev/null 2>&1
    /sbin/service sympasoap stop >/dev/null 2>&1
    /sbin/chkconfig --del wwsympa
    /sbin/chkconfig --del sympasoap
fi
%endif

%post nginx
# register service
%if %{use_systemd}
%systemd_post wwsympa.service
%systemd_post sympasoap.service
%else
/sbin/chkconfig --add wwsympa
/sbin/chkconfig --add sympasoap
%endif

%postun nginx
%if %{use_systemd}
%systemd_postun_with_restart wwsympa.service
%systemd_postun_with_restart sympasoap.service
%else
if [ "$1" -ge "1" ] ; then
    /sbin/service wwsympa condrestart >/dev/null 2>&1 || :
    /sbin/service sympasoap condrestart >/dev/null 2>&1 || :
fi
%endif


%files -f %{name}.lang -f web_help.lang
%doc __doc/*
%license COPYING
%dir %attr(-,sympa,sympa) %{_sysconfdir}/sympa/
%{_sysconfdir}/sympa/README
%config(noreplace) %attr(0640,sympa,sympa) %{_sysconfdir}/sympa/sympa.conf
%config(noreplace,missingok) %attr(-,sympa,sympa) %{_sysconfdir}/sympa/auth.conf
%config(noreplace,missingok) %attr(-,sympa,sympa) %{_sysconfdir}/sympa/charset.conf
%config(noreplace,missingok) %attr(-,sympa,sympa) %{_sysconfdir}/sympa/crawlers_detection.conf
%config(noreplace,missingok) %attr(-,sympa,sympa) %{_sysconfdir}/sympa/create_list.conf
%config(noreplace,missingok) %attr(-,sympa,sympa) %{_sysconfdir}/sympa/edit_list.conf
%config(noreplace,missingok) %attr(-,sympa,sympa) %{_sysconfdir}/sympa/nrcpt_by_domain.conf
%config(noreplace,missingok) %attr(-,sympa,sympa) %{_sysconfdir}/sympa/topics.conf
%config(noreplace,missingok) %attr(-,sympa,sympa) %{_sysconfdir}/sympa/mime.types
%config(noreplace,missingok) %attr(-,sympa,sympa) %{_sysconfdir}/sympa/sympa.wsdl
%dir %attr(-,sympa,sympa) %{_sysconfdir}/sympa/create_list_templates
%dir %attr(-,sympa,sympa) %{_sysconfdir}/sympa/tasks
%dir %attr(-,sympa,sympa) %{_sysconfdir}/sympa/scenari
%dir %attr(-,sympa,sympa) %{_sysconfdir}/sympa/mail_tt2
%dir %attr(-,sympa,sympa) %{_sysconfdir}/sympa/web_tt2
%dir %attr(-,sympa,sympa) %{_sysconfdir}/sympa/custom_actions
%dir %attr(-,sympa,sympa) %{_sysconfdir}/sympa/custom_conditions
%dir %attr(-,sympa,sympa) %{_sysconfdir}/sympa/data_sources
%dir %attr(-,sympa,sympa) %{_sysconfdir}/sympa/families
%dir %attr(-,sympa,sympa) %{_sysconfdir}/sympa/search_filters
%config(missingok) %attr(-,sympa,sympa) %{_sysconfdir}/sympa/data_structure.current_version
%config(noreplace) %{_sysconfdir}/sympa/aliases.sympa.sendmail
%config(noreplace) %{_sysconfdir}/sympa/aliases.sympa.sendmail.db
%config(noreplace) %{_sysconfdir}/sympa/aliases.sympa.postfix
%config(noreplace) %{_sysconfdir}/sympa/aliases.sympa.postfix.db
%{_sysconfdir}/smrsh/*
%config(noreplace) %{_sysconfdir}/rsyslog.d/*
%config(noreplace) %{_sysconfdir}/logrotate.d/sympa
%{_sbindir}/*
%dir %{_libexecdir}/sympa/
%attr(4755,sympa,sympa) %{_libexecdir}/sympa/bouncequeue
%attr(4755,sympa,sympa) %{_libexecdir}/sympa/familyqueue
%attr(4755,sympa,sympa) %{_libexecdir}/sympa/queue
%attr(4750,root,sympa) %{_libexecdir}/sympa/sympa_newaliases-wrapper
%{_libexecdir}/sympa/sympa_soap_server.fcgi
%attr(6755,sympa,sympa) %{_libexecdir}/sympa/sympa_soap_server-wrapper.fcgi
%{_libexecdir}/sympa/wwsympa.fcgi
%attr(6755,sympa,sympa) %{_libexecdir}/sympa/wwsympa-wrapper.fcgi
%attr(-,sympa,sympa) %{_localstatedir}/lib/sympa/
%attr(-,sympa,sympa) %{_localstatedir}/spool/sympa/
%{_datadir}/sympa/
%{_mandir}/man1/*
%{_mandir}/man5/*
%{_mandir}/man8/*
%if %{use_systemd}
%{_unitdir}/sympa.service
%{_unitdir}/sympa-outgoing.service
%{_unitdir}/sympa-archive.service
%{_unitdir}/sympa-bounce.service
%{_unitdir}/sympa-task.service
%{_tmpfilesdir}/sympa.conf
%ghost %attr(-,sympa,sympa) %{_rundir}/sympa/
%dir %{_sysconfdir}/systemd/system/sympa.service.d/
%config(noreplace) %{_sysconfdir}/systemd/system/sympa.service.d/*
%else
%{_initrddir}/sympa
%attr(-,sympa,sympa) %{_localstatedir}/run/sympa/
%endif
%config(noreplace) %{_sysconfdir}/sysconfig/sympa


%files httpd
%config(noreplace) %{_sysconfdir}/httpd/conf.d/sympa.conf
%if 0%{?fedora} || 0%{?rhel} >= 7
%if %{use_systemd}
%{_unitdir}/wwsympa.service
%{_unitdir}/sympasoap.service
%else
%{_initrddir}/wwsympa
%{_initrddir}/sympasoap
%endif
%endif


%files lighttpd
%config(noreplace) %{_sysconfdir}/lighttpd/conf.d/sympa.conf


%files nginx
%config(noreplace) %{_sysconfdir}/nginx/conf.d/sympa.conf
%if %{use_systemd}
%{_unitdir}/wwsympa.service
%{_unitdir}/sympasoap.service
%else
%{_initrddir}/wwsympa
%{_initrddir}/sympasoap
%endif


%files devel-doc
%{_mandir}/man3/*


%changelog
* Tue Oct 20 2020 Xavier Bachelot <xavier@bachelot.org> 6.2.58-1
- Update to 6.2.58

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.56-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 13 2020 Xavier Bachelot <xavier@bachelot.org> 6.2.56-2
- Prepare for some js packages retirement in Fedora

* Sun May 24 2020 Xavier Bachelot <xavier@bachelot.org> 6.2.56-1
- Update to 6.2.56 (Fixes CVE-2020-10936)
- Fix typo in url and also socket location in lighttpd configuration (RHBZ#1812325)

* Mon Mar 02 2020 Xavier Bachelot <xavier@bachelot.org> 6.2.54-1
- Update to 6.2.54 (Fixes CVE-2020-9369).

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.52-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Xavier Bachelot <xavier@bachelot.org> 6.2.52-2
- Add upstream patches to fix 2 scenario failures.

* Fri Dec 27 2019 Xavier Bachelot <xavier@bachelot.org> 6.2.52-1
- Update to 6.2.52.

* Sun Dec 22 2019 Xavier Bachelot <xavier@bachelot.org> 6.2.50-1
- Update to 6.2.50.
- Re-enable Crypt::OpenSSL::X509 for EL8.

* Fri Nov 29 2019 Xavier Bachelot <xavier@bachelot.org> 6.2.48-3
- Add patch to fix compile executables test on F32.
- Add dependency on Socket6 and IO::Socket::IP
  (or alternatively Socket6 and IO::Socket::INET6 on EL6).
- Add patch to fix ldap 2 level query.
- Re-enable Crypt::SMIME for EL8.
- Re-enable all web subpackages for EL8.

* Wed Oct 16 2019 Xavier Bachelot <xavier@bachelot.org> 6.2.48-2
- Don't require optional perl modules unavailable on EL8.
- Disable httpd and lighttpd support for EL8 until missing bits are available.
- Change sympa localstatedir owner/group to sympa:sympa. Fixes RHBZ#1761455.

* Mon Sep 30 2019 Xavier Bachelot <xavier@bachelot.org> 6.2.48-1
- Update to 6.2.48.

* Mon Sep 23 2019 Xavier Bachelot <xavier@bachelot.org> 6.2.46-1
- Update to 6.2.46.
- Unbundle foundation-icons font.
- Add dependency on LWP::Protocol::https (RHBZ#1753111).
- Don't unbundle js-respond on EL8 (yet).

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.44-3.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 18 2019 Xavier Bachelot <xavier@bachelot.org> 6.2.44-3
- Don't build for ix86 on EL6.
- Re-order some parts of spec for better readability.
- Use bcond_with macro instead of custom macros.

* Mon Jul 15 2019 Xavier Bachelot <xavier@bachelot.org> 6.2.44-2
- Don't package OChangeLog and ONEWS. Saves 5MB.
- Move developers documentation to devel-doc sub-package.
- Compute an accurate License: tag.

* Wed Jun 26 2019 Xavier Bachelot <xavier@bachelot.org> 6.2.44-1
- Update to 6.2.44.

* Mon Jun 10 2019 Xavier Bachelot <xavier@bachelot.org> 6.2.43-0.2.b.2
- Update to 6.2.43 beta 2.

* Thu May 23 2019 IKEDA Soji <ikeda@conversion.co.jp> 6.2.43-0.1.b.1
- Update to 6.2.43 beta 1.
- Move sympa.conf-dist to doc.

* Thu Mar 21 2019 Xavier Bachelot <xavier@bachelot.org> 6.2.42-1
- Update to 6.2.42.

* Sun Mar 10 2019 Xavier Bachelot <xavier@bachelot.org> 6.2.41-0.2.b.2
- Update to 6.2.41 beta 2.

* Sun Feb 03 2019 Xavier Bachelot <xavier@bachelot.org> 6.2.41-0.1.b.1
- Update to 6.2.41 beta 1.

* Mon Jan 28 2019 Xavier Bachelot <xavier@bachelot.org> 6.2.40-2
- Unbundle jqplot on F29+.
- Use versioned Requires and BuildRequires for unbundled fonts and libs.

* Sat Jan 19 2019 Xavier Bachelot <xavier@bachelot.org> 6.2.40-1
- Update to 6.2.40.

* Fri Jan 11 2019 Xavier Bachelot <xavier@bachelot.org> 6.2.38-2
- Fix fontawesome, jquery-ui and jquery-migrate unbundling on EL7.
- Fix wwsympa/sympasoap not being restarted on update.

* Fri Dec 21 2018 Xavier Bachelot <xavier@bachelot.org> 6.2.38-1
- Update to 6.2.38.

* Sat Dec 08 2018 Xavier Bachelot <xavier@bachelot.org> 6.2.37-0.3.b.3
- Update to 6.2.37 beta 3.

* Sat Nov 03 2018 Xavier Bachelot <xavier@bachelot.org> 6.2.37-0.2.b.2
- Update to 6.2.37 beta 2.

* Sun Oct 07 2018 Xavier Bachelot <xavier@bachelot.org> 6.2.37-0.1.b.1
- Update to 6.2.37 beta 1.

* Sun Sep 23 2018 IKEDA Soji <ikeda@conversion.co.jp> 6.2.36-1
- Update to 6.2.36.

* Sun Aug 26 2018 IKEDA Soji <ikeda@conversion.co.jp> 6.2.35-0.1.b.1
- Update to 6.2.35b.1.
- For sympa-httpd with Fedora & EL7: Use mod_proxy_fcgi instead of mod_fcgid.

* Sun Aug 26 2018 IKEDA Soji <ikeda@conversion.co.jp> 6.2.34-2
- Issue #36: Init scripts for wwsympa/sympasoap were broken.

* Thu Jul 05 2018 Xavier Bachelot <xavier@bachelot.org> 6.2.34-1
- Update to 6.2.34.

* Fri Jun 29 2018 IKEDA Soji <ikeda@conversion.co.jp> 6.2.33-0.2.b.2
- Update to 6.2.33 beta 2.
  Upstream #170 WWSympa: Switch to Foundation 6
  Upstream #220 static_content directory structure
  Upstream #336 Starting a test framework

* Wed Apr 25 2018 Xavier Bachelot <xavier@bachelot.org> 6.2.32-2
- Add missing Requires on EL6 and EL7.

* Thu Apr 19 2018 Xavier Bachelot <xavier@bachelot.org> 6.2.32-1
- Update to 6.2.32 (Security release).
  See https://sympa-community.github.io/security/2018-001.html

* Mon Mar 26 2018 Xavier Bachelot <xavier@bachelot.org> 6.2.30-1
- Update to 6.2.30.

* Thu Mar 22 2018 Xavier Bachelot <xavier@bachelot.org> 6.2.28-1
- Update to 6.2.28.

* Tue Mar 20 2018 Xavier Bachelot <xavier@bachelot.org> 6.2.26-1
- Update to 6.2.26.
- Fix scriptlet.

* Tue Mar 13 2018 Xavier Bachelot <xavier@bachelot.org> 6.2.25-0.3.b.3
- Update to 6.2.25 beta 3.
- Add Requires on optional Crypt::Eksblowfish.

* Mon Mar 05 2018 Xavier Bachelot <xavier@bachelot.org> 6.2.25-0.2.b.2
- Update to 6.2.25 beta 2.
- Move static_content to an FHS compliant location.

* Tue Feb 13 2018 Xavier Bachelot <xavier@bachelot.org> 6.2.25-0.1.b.1
- Update to 6.2.25 beta 1.
- Remove useless and bogus directories creation for conf override.
- Own the now properly created css and pictures directories.
  Subsequently the above directory doesn't need to be writable anymore.
- Unbundle Raleway font.
- Simplify sysvinit/systemd in configure.

* Tue Dec 26 2017 Xavier Bachelot <xavier@bachelot.org> 6.2.24-2
- Ensure newaliases works out of the box.

* Thu Dec 21 2017 Xavier Bachelot <xavier@bachelot.org> 6.2.24-1
- Update to 6.2.24.

* Thu Dec 14 2017 Xavier Bachelot <xavier@bachelot.org> 6.2.23-0.4.b.3
- Update to 6.2.23 beta 3.

* Tue Dec 12 2017 Xavier Bachelot <xavier@bachelot.org> 6.2.23-0.4.b.2
- Unbundle jquery (Fedora only).

* Thu Nov 30 2017 Xavier Bachelot <xavier@bachelot.org> 6.2.23-0.3.b.2
- Update to 6.2.23 beta 2.

* Wed Nov 22 2017 Xavier Bachelot <xavier@bachelot.org> 6.2.23-0.2.b.1
- Specify all build dependencies. Fixes test suite failure on F25/F26.

* Mon Nov 20 2017 Xavier Bachelot <xavier@bachelot.org> 6.2.23-0.1.b.1
- Update to 6.2.23 beta 1.
- Drop upstream patches.
- Add missing BuildRequires:.
- Remove duplicate Requires:.
- Fix License: to acknowledge for bundled javascript libraries.
- Track more bundled javascript libraries.

* Wed Nov 08 2017 Xavier Bachelot <xavier@bachelot.org> 6.2.22-4
- Run autoreconf for jquery patch.

* Wed Oct 25 2017 Xavier Bachelot <xavier@bachelot.org> 6.2.22-3
- Fix scriplet bug in upgrade_data_structure.
- Unbundle font-awesome.

* Fri Oct 20 2017 Xavier Bachelot <xavier@bachelot.org> 6.2.22-2
- Add patches from upstream sympa-6.2 branch.

* Tue Oct 03 2017 Xavier Bachelot <xavier@bachelot.org> 6.2.22-1
- Update to 6.2.22.

* Thu Sep 14 2017 Xavier Bachelot <xavier@bachelot.org> 6.2.19-0.2.b.2
- Rework spec to better comply with Fedora packaging guidelines.

* Sat Aug 19 2017 IKEDA Soji <ikeda@conversion.co.jp> 6.2.19b.1-1
- Added --bindir to install sympa_smtpc under libexecdir.

* Sun Jun 25 2017 IKEDA Soji <ikeda@conversion.co.jp> 6.2.18-1
- Updated.

* Thu Jun 15 2017 IKEDA Soji <ikeda@conversion.co.jp> 6.2.17b.2-1
- Updated README.RPM.md.

* Sun Aug 07 2016 IKEDA Soji <ikeda@conversion.co.jp> 6.2.17-1
- Typos in el6-README.RPM.
- Added a build dependency perl(Test::Harness).
- Added a dependency perl(Unicode::Normalize).
- Added a definition parameter %%{do_autoreconf}.

* Sat Jun 18 2016 IKEDA Soji <ikeda@conversion.co.jp> 6.2.16-1
- Adopted adjustment to Fedora by Xavier Bachelot <xavier@bachelot.org>.
- Avoiding use of buildroot macro in build section.
- Simplified configure option.
- Added patch14 to disable service by default.
- Added unit customization file source129.

* Thu Feb 26 2015 IKEDA Soji <ikeda@conversion.co.jp> 6.2-1
- New minor release sympa-6.2.
