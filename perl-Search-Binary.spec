%include	/usr/lib/rpm/macros.perl
Summary:	Search-Binary perl module
Summary(pl):	Modu³ perla Search-Binary
Name:		perl-Search-Binary
Version:	0.95
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Search/Search-Binary-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Search-Binary - generic binary search.

%description -l pl
Search-Binary - podstawowe wyszukiwanie binarne.

%prep
%setup -q -n Search-Binary-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf ChangeLog README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Search/Binary.pm
%{_mandir}/man3/*
