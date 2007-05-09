#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	HTML
%define	pnam	Entities-Numbered
Summary:	HTML::Entities::Numbered - Conversion of numbered HTML entities
Summary(pl.UTF-8):	HTML::Entities::Numbered - konwersja numerycznych elementów HTML-a
Name:		perl-HTML-Entities-Numbered
Version:	0.04
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/HTML/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9bc61132c10aa506d2629b37a2012729
URL:		http://search.cpan.org/dist/HTML-Entities-Numbered/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTML::Entities::Numbered is a content conversion filter for named HTML
entities (symbols, mathmetical symbols, Greek letters, Latin letters,
etc.).

%description -l pl.UTF-8
HTML::Entities::Numbered to filtr do konwersji treści dla nazwanych
elementów HTML-a (symboli, symboli matematycznych, liter greckich,
liter łacińskich itp.).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/HTML/Entities
%{_mandir}/man3/*
